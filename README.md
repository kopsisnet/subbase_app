## 📄 `README.md` – Django + Supabase + Render Yayın Süreci

```markdown
# 🧵 KopsisNet – Django Üretim Sistemi

Bu proje, Django ile geliştirilmiş bir üretim yönetim sistemidir. Supabase veritabanı kullanır ve Render üzerinden yayına alınmıştır.

---

## 🚀 Kurulum ve Geliştirme Ortamı

### 1. Python Ortamı Oluştur

```bash
python -m venv myenv
source myenv/bin/activate  # Windows: myenv\Scripts\activate
```

### 2. Gerekli Paketleri Kur

```bash
pip install django psycopg2-binary dj-database-url whitenoise
pip freeze > requirements.txt
```

---

## 🛠️ Django Projesi Oluşturma

```bash
django-admin startproject subbase_app .
python manage.py startapp urunler
```

---

## ⚙️ `settings.py` Yapılandırması

### Veritabanı Ayarı (Supabase)

```python
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}
```

### Static Dosyalar

```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]
```

### Güvenlik Ayarları

```python
ALLOWED_HOSTS = ['subbase-app.onrender.com']
SECRET_KEY = os.environ.get('SECRET_KEY', 'dummy-key')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
```

---

## 🧪 Veritabanı Migrasyonları

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🧑‍💻 GitHub’a Yükleme

### Git Başlat

```bash
git init
git remote add origin https://github.com/kopsis/kopsisnet.git
```

### Kullanıcı Bilgisi Ayarla

```bash
git config --global user.name "kopsis"
git config --global user.email "kopsis@example.com"
```

### Commit ve Push

```bash
git add .
git commit -m "İlk yükleme"
git push -u origin main
```

---

## 🌐 Render Yayına Alma

### Web Service Oluştur

- GitHub reposunu Render’a bağla
- Build Command:  
  ```bash
  pip install -r requirements.txt
  ```
- Start Command:  
  ```bash
  gunicorn subbase_app.wsgi:application
  ```

### Ortam Değişkenleri Tanımla

| Anahtar         | Değer (örnek)                                      |
|------------------|----------------------------------------------------|
| `DEBUG`          | `False`                                            |
| `SECRET_KEY`     | `django-insecure-...`                              |
| `DATABASE_URL`   | `postgresql://...` (Supabase bağlantı dizesi)      |
| `ALLOWED_HOSTS`  | `subbase-app.onrender.com`                         |

---

## ✅ Yayın Testi

- Uygulama adresi: `https://subbase-app.onrender.com`
- Supabase Dashboard üzerinden veri kontrolü
- TailwindCSS ile responsive arayüz

---

## 📦 Ekstra

- `.env` dosyasını `.gitignore` ile dışla
- `README.md` dosyasını güncel tut
- Domain bağlama için Render DNS ayarlarını kullan

---

## 🧠 Katkı ve Geliştirme

Pull request’ler ve öneriler memnuniyetle karşılanır.  
Bu proje KOPSIS tarafından geliştirilmiştir.
```

---

İstersen bu `README.md` dosyasını GitHub repo köküne ekleyebilirim veya Markdown formatında daha sade bir versiyonunu da hazırlayabilirim. Ayrıca domain bağlama, CI/CD entegrasyonu veya Supabase Auth için ek bölümler de ekleyebilirim. Devam edelim mi?
