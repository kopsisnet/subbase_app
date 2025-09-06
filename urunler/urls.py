from django.urls import path
from . import views

urlpatterns = [
    path('', views.urun_listesi, name='urun_listesi'),
    path('ekle/', views.urun_ekle, name='urun_ekle'),
    path('<int:pk>/guncelle/', views.urun_guncelle, name='urun_guncelle'),
    path('<int:pk>/detay/', views.urun_detay, name='urun_detay'),
    path('<int:pk>/sil/', views.urun_sil, name='urun_sil'),
]
