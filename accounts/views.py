from django.shortcuts import render, redirect
from .utils.supabase_auth import (
    get_user_info, login_user, signup_user, reset_password,
    update_password, is_authorized, insert_user_record
)

def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        result = login_user(email, password)
        if "access_token" in result:
            user_id = result["user"]["id"]
            if is_authorized(user_id):
                request.session["token"] = result["access_token"]
                request.session["user_id"] = user_id
                return redirect("urun_listesi")
            else:
                return render(request, "accounts/unauthorized.html")
        return render(request, "accounts/login.html", {"error": result.get("error_description")})
    return render(request, "accounts/login.html")

def logout_view(request):
    request.session.flush()
    return redirect("login")

def signup_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        result = signup_user(email, password)

        print("📩 Supabase signup yanıtı: %s", result)

        # Supabase e-posta doğrulama açıkken doğrudan user objesi döner
        user_info = result
        user_id = user_info.get("id")

        if user_id:
            print("✅ user.id bulundu: %s", user_id)
            insert_user_record(user_id, email)
            return render(request, "accounts/signup.html", {
                "success": "Kayıt başarılı. E-posta doğrulaması sonrası giriş yapabilirsiniz."
            })

        # Eğer access_token varsa yine kullanıcı bilgisi çekilebilir
        token = result.get("access_token")
        if token:
            user_info = get_user_info(token)
            print("🔐 Token ile çekilen kullanıcı: %s", user_info)
            user_id = user_info.get("id")
            if user_id:
                insert_user_record(user_id, email)
                return render(request, "accounts/signup.html", {
                    "success": "Kayıt başarılı. Admin onayı sonrası giriş yapabilirsiniz."
                })

        error_msg = result.get("error_description") or result.get("msg") or "Kayıt başarısız."
        print("❌ Kayıt hatası: %s", error_msg)
        return render(request, "accounts/signup.html", {"error": error_msg})
    return render(request, "accounts/signup.html")


def reset_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        result = reset_password(email)
        if "error" in result:
            return render(request, "accounts/reset.html", {"error": result["error_description"]})
        return render(request, "accounts/reset.html", {"success": "Şifre sıfırlama bağlantısı gönderildi."})
    return render(request, "accounts/reset.html")

def update_password_view(request):
    token = request.GET.get("access_token")
    if request.method == "POST":
        new_password = request.POST["new_password"]
        result = update_password(token, new_password)
        if "error" in result:
            return render(request, "accounts/update_password.html", {"error": result["error_description"]})
        return redirect("login")
    return render(request, "accounts/update_password.html")
