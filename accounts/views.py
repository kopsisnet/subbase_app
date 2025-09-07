from django.shortcuts import render, redirect
from .utils.supabase_auth import login_user, signup_user, reset_password, update_password, is_authorized

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
        if "access_token" in result:
            return render(request, "accounts/signup.html", {
                "success": "Kayıt başarılı. Admin onayı sonrası giriş yapabilirsiniz."
            })
        return render(request, "accounts/signup.html", {"error": result.get("error_description")})
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
