from django import forms
from .models import Urun

class UrunForm(forms.ModelForm):
    class Meta:
        model = Urun
        fields = ['ad', 'fiyat', 'stok', 'aciklama']
        labels = {
            'ad': 'Ürün Adı',
            'fiyat': 'Fiyat (₺)',
            'stok': 'Stok Miktarı',
            'aciklama': 'Açıklama'
        }
        widgets = {
            'ad': forms.TextInput(attrs={'class': 'form-input'}),
            'fiyat': forms.NumberInput(attrs={'class': 'form-input'}),
            'stok': forms.NumberInput(attrs={'class': 'form-input'}),
            'aciklama': forms.Textarea(attrs={'class': 'form-textarea'}),
        }
