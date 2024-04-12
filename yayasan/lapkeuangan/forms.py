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
            'tanggal_transaksi', 
            'nomer_transaksi', 
            'urutan_transaksi', 
            'no_bukti_transaksi', 
            'organisasi', 
            'unitowner_id', 
            'unitowner_nama', 
            'entitas_id', 
            'entitas_nama', 
            'program_id', 
            'program_nama', 
            'akun_kode', 
            'akun_nama', 
            'keterangan_transaksi', 
            'nominal_debet', 
            'nominal_kredit', 
            'catatan'             
        ]        