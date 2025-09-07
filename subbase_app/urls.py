from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Ürün yönetimi uygulaması (ana sayfa)
    path('', include('urunler.urls')),

    # Kullanıcı işlemleri (giriş, kayıt, şifre vs)
    path('accounts/', include('accounts.urls')),
]
