from django.shortcuts import render, redirect
import requests

from subbase_app.settings import SUPABASE_URL
from .utils.supabase_auth import (
    HEADERS, signup_user, login_user, get_user_info, update_password,
    reset_password, insert_user_record, is_authorized, get_user_roles
)
import logging
logger = logging.getLogger(__name__)

def signup_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        ad = request.POST.get("ad")
        result = signup_user(email, password)
        user_id = result.get("id") or result.get("user", {}).get("id")
        if user_id:
            insert_user_record(user_id, email, ad=ad)
            return render(request, "accounts/signup.html", {
                "success": "Kayıt başarılı. E-posta doğrulaması sonrası giriş yapabilirsiniz."
            })
        error_msg = result.get("error_description") or result.get("msg") or "Kayıt başarısız."
        return render(request, "accounts/signup.html", {"error": error_msg})
    return render(request, "accounts/signup.html")

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
                return redirect("dashboard")
            else:
                return render(request, "accounts/unauthorized.html")
        return render(request, "accounts/login.html", {"error": result.get("error_description")})
    return render(request, "accounts/login.html")

def set_password_view(request):
    token = request.GET.get("access_token")
    if not token:
        return render(request, "accounts/set_password.html", {"error": "Geçersiz bağlantı."})
    if request.method == "POST":
        new_password = request.POST["new_password"]
        result = update_password(token, new_password)
        if "error" in result:
            return render(request, "accounts/set_password.html", {"error": result["error_description"]})
        return redirect("login")
    return render(request, "accounts/set_password.html")

def reset_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        result = reset_password(email)
        if "error" in result:
            return render(request, "accounts/reset.html", {"error": result["error_description"]})
        return render(request, "accounts/reset.html", {"success": "Şifre sıfırlama bağlantısı gönderildi."})
    return render(request, "accounts/reset.html")

def admin_users_view(request):
    url = f"{SUPABASE_URL}/kopsis_users?select=id,email,aktif,rol_id,ad"
    response = requests.get(url, headers=HEADERS)
    users = response.json()
    return render(request, "admin/users.html", {"users": users})

def admin_update_user_view(request, user_id):
    if request.method == "POST":
        aktif = request.POST.get("aktif") == "on"
        rol_id = request.POST.get("rol_id")
        url = f"{SUPABASE_URL}/kopsis_users?id=eq.{user_id}"
        payload = {"aktif": aktif, "rol_id": int(rol_id)}
        response = requests.patch(url, json=payload, headers=HEADERS)
        return redirect("admin_users")
