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
            'owner_program', 'organisasi', 'kode_akun', 'entitas', 'tanggal_transaksi',
            'nominal_debet', 'nominal_kredit', 'catatan', 'program', 'keterangan_transaksi'
        ]        