from django.db import models
from yayasan.program.models import ProgramKerja
from yayasan.institusi.models import Institusi, Unit
from yayasan.entitas.models import Entitas
from core.models import TimeStampedModel


class KodeAkun(models.Model):
    kode_akun = models.CharField(max_length=100)
    nama_akun = models.CharField(max_length=100)
    institusi = models.ForeignKey(Institusi, on_delete=models.CASCADE)
    DEBET_OR_KREDIT_CHOICES = [
        ('debet', 'Debet'),
        ('kredit', 'Kredit'),
    ]
    debet_or_kredit = models.CharField(
        max_length=100, choices=DEBET_OR_KREDIT_CHOICES)
    KATEGORI_CHOICES = [
        ('neraca', 'Neraca'),
        ('labarugi', 'Laba Rugi'),
    ]
    kategori_pembukuan = models.CharField(
        max_length=100, choices=KATEGORI_CHOICES)
    pasangan_akun = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True)
    catatan = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nama_akun

class JurnalTransaksi(TimeStampedModel):
    tanggal_transaksi = models.DateField()
    nomer_transaksi = models.CharField(max_length=100) # Nomer urutan dalam satu bulan
    urutan_transaksi = models.CharField(max_length=100) # Urutan transaksi per kode akun
    no_bukti_transaksi = models.CharField(max_length=100) # Nomer bukti transaksi cetak macam kuitansi
    organisasi = models.ForeignKey(Institusi, on_delete=models.CASCADE)
    unitowner_id = models.ForeignKey(Unit, related_name="jurnaltransaksi_unit_owner", on_delete=models.CASCADE) # unit yang melakukan transaksi
    unitowner_nama = models.CharField(max_length=100, null=True, blank=True)
    entitas_id = models.ForeignKey(Entitas, related_name="jurnaltransaksi_entitas_transaksi", on_delete=models.CASCADE)   # subyek transaksi 
    entitas_nama = models.CharField(max_length=100, null=True, blank=True)  # Untuk keperluan export ke excel
    program_id = models.ForeignKey(ProgramKerja, related_name="jurnaltransaksi_program", on_delete=models.CASCADE)
    program_nama = models.CharField(max_length=100, null=True, blank=True) # Untuk keperluan export ke excel
    akun_kode = models.ForeignKey(KodeAkun, related_name="jurnaltransaksi_akun_kode",on_delete=models.CASCADE)
    akun_nama = models.CharField(max_length=100) # Untuk keperluan export ke excel
    keterangan_transaksi = models.CharField(max_length=100, null=True, blank=True) # secara langsung menjelaskan transaksi
    nominal_debet = models.DecimalField(
        max_digits=25, decimal_places=2, default=0.00)
    nominal_kredit = models.DecimalField(
        max_digits=25, decimal_places=2, default=0.00)
    catatan = models.TextField(null=True, blank=True)
