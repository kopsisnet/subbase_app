from django.contrib import admin
from .models import Urun

@admin.register(Urun)
class UrunAdmin(admin.ModelAdmin):
    list_display = ("ad", "fiyat", "stok", "eklenme_tarihi")
    search_fields = ("ad",)
