from django.db import models

class Urun(models.Model):
    ad = models.CharField("Ürün Adı", max_length=100)
    fiyat = models.DecimalField("Fiyat (₺)", max_digits=10, decimal_places=2)
    stok = models.IntegerField("Stok Miktarı")
    aciklama = models.TextField("Açıklama", blank=True)
    eklenme_tarihi = models.DateTimeField("Eklenme Tarihi", auto_now_add=True)

    def __str__(self):
        return self.ad
