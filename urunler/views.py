from django.shortcuts import render, get_object_or_404, redirect
from .models import Urun
from .forms import UrunForm

def urun_listesi(request):
    urunler = Urun.objects.all().order_by('-eklenme_tarihi')
    return render(request, 'urunler/liste.html', {'urunler': urunler})

def urun_ekle(request):
    form = UrunForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('urun_listesi')
    return render(request, 'urunler/form.html', {
        'form': form,
        'baslik': 'Yeni Ürün Ekle',
        'buton_metni': 'Kaydet'
    })

def urun_guncelle(request, pk):
    urun = get_object_or_404(Urun, pk=pk)
    form = UrunForm(request.POST or None, instance=urun)
    if form.is_valid():
        form.save()
        return redirect('urun_listesi')
    return render(request, 'urunler/form.html', {
        'form': form,
        'baslik': 'Ürünü Güncelle',
        'buton_metni': 'Güncelle'
    })

def urun_detay(request, pk):
    urun = get_object_or_404(Urun, pk=pk)
    return render(request, 'urunler/detay.html', {'urun': urun})

def urun_sil(request, pk):
    urun = get_object_or_404(Urun, pk=pk)
    if request.method == 'POST':
        urun.delete()
        return redirect('urun_listesi')
    return render(request, 'urunler/sil.html', {'urun': urun})
