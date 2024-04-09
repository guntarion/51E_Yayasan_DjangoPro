from django.db import models
from yayasan.program.models import ProgramKerja
from yayasan.institusi.models import Institusi
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
    nomer_transaksi = models.CharField(max_length=100)
    organisasi = models.ForeignKey(Institusi, on_delete=models.CASCADE)
    entitas = models.ForeignKey(
        Entitas, related_name="entitas_transaksi", on_delete=models.CASCADE)
    urutan_transaksi = models.CharField(max_length=100)
    no_bukti_transaksi = models.CharField(max_length=100)
    program = models.ForeignKey(ProgramKerja, on_delete=models.CASCADE)
    tanggal_transaksi = models.DateField()
    kode_akun = models.ForeignKey(KodeAkun, on_delete=models.CASCADE)
    nama_akun = models.CharField(max_length=100)
    keterangan = models.TextField()
    jumlah = models.DecimalField(max_digits=25, decimal_places=2, default=0.00)
    DEBET_OR_KREDIT_CHOICES = [
        ('debet', 'Debet'),
        ('kredit', 'Kredit'),
    ]
    debet_or_kredit = models.CharField(
        max_length=100, choices=DEBET_OR_KREDIT_CHOICES)
    nominal_debet = models.DecimalField(
        max_digits=25, decimal_places=2, default=0.00)
    nominal_kredit = models.DecimalField(
        max_digits=25, decimal_places=2, default=0.00)
    catatan = models.TextField(null=True, blank=True)
