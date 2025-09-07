import requests
from django.conf import settings

SUPABASE_AUTH_URL = f"{settings.SUPABASE_URL}/auth/v1"
SUPABASE_DB_URL = f"{settings.SUPABASE_URL}/rest/v1"
HEADERS = {
    "apikey": settings.SUPABASE_KEY,
    "Content-Type": "application/json"
}

def login_user(email, password):
    url = f"{SUPABASE_AUTH_URL}/token?grant_type=password"
    response = requests.post(url, json={"email": email, "password": password}, headers=HEADERS)
    return response.json()

def signup_user(email, password):
    url = f"{SUPABASE_AUTH_URL}/signup"
    response = requests.post(url, json={"email": email, "password": password}, headers=HEADERS)
    return response.json()

def reset_password(email):
    url = f"{SUPABASE_AUTH_URL}/recover"
    response = requests.post(url, json={
        "email": email,
        "redirect_to": "https://subbase-app.onrender.com/update-password"
    }, headers=HEADERS)
    return response.json()

def update_password(token, new_password):
    url = f"{SUPABASE_AUTH_URL}/user"
    headers = HEADERS.copy()
    headers["Authorization"] = f"Bearer {token}"
    response = requests.put(url, json={"password": new_password}, headers=headers)
    return response.json()

def is_authorized(user_id):
    url = f"{SUPABASE_DB_URL}/kopsis_users?id=eq.{user_id}&select=aktif"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        return False
    data = response.json()
    return bool(data) and data[0].get("aktif", False)

def insert_user_record(user_id, email):
    url = f"{SUPABASE_DB_URL}/kopsis_users"
    payload = {
        "id": user_id,
        "email": email,
        "aktif": False
    }
    headers = HEADERS.copy()
    headers["Prefer"] = "return=minimal"
    requests.post(url, json=payload, headers=headers)

def get_user_info(token):
    url = f"{SUPABASE_AUTH_URL}/user"
    headers = HEADERS.copy()
    headers["Authorization"] = f"Bearer {token}"
    response = requests.get(url, headers=headers)
    return response.json()