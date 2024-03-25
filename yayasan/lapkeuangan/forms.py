# forms.py
from django import forms
from .models import KodeAkun, JurnalTransaksi
from yayasan.institusi.models import Unit

class KodeAkunForm(forms.ModelForm):
    class Meta:
        model = KodeAkun
        fields = '__all__'

class JurnalTransaksiForm(forms.ModelForm):
    # owner_program = forms.ModelChoiceField(
    #     queryset=Unit.objects.all().distinct('namaUnit'))
    owner_program = forms.ModelChoiceField(
        queryset=Unit.objects.values_list('namaUnit', flat=True).distinct())
    
    class Meta:
        model = JurnalTransaksi
        fields = [
            'owner_program', 'kode_akun', 'organisasi', 'nomer_transaksi', 'entitas',
            'urutan_per_kode_akun', 'tanggal_transaksi', 'keterangan', 
            'jumlah', 'debet_or_kredit', 'nominal_debet', 'nominal_kredit', 
            'catatan'
        ]        