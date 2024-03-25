from django.db import models
from django.utils import timezone
from django.db.models import F

from yayasan.institusi.models import Unit

from django.core.validators import MaxValueValidator, MinValueValidator
from core.models import TimeStampedModel


class ProgramKerja(TimeStampedModel):
    TER = 'TER'
    BEB = 'BEB'
    OUT = 'OUT'
    JENIS_INPUT_OUTPUT_CHOICES = [
        (TER, 'Input Terikat'),
        (BEB, 'Input Bebas'),
        (OUT, 'Output'),
    ]

    NON_ASSET = 'nonAsset'
    YES_ASSET = 'yesAsset'
    JENIS_PROGRAM_CHOICES = [
        (NON_ASSET, 'Non Asset'),
        (YES_ASSET, 'Asset'),
    ]

    PERIODE_BULAN = 'bulan'
    PERIODE_TAHUN = 'tahun'
    PERIODE_CHOICES = [
        (PERIODE_BULAN, 'Bulan'),
        (PERIODE_TAHUN, 'Tahun'),
    ]

    SIFAT_FIKS = 'fiks'
    SIFAT_FLEKSIBEL = 'fleksibel'
    SIFAT_PERIODE_CHOICES = [
        (SIFAT_FIKS, 'Fiks'),
        (SIFAT_FLEKSIBEL, 'Fleksibel'),
    ]

    TERENCANA = 'terencana'
    MODIFIKASI = 'modifikasi'
    USULANBARU = 'usulanbaru'
    DIPERTIMBANGKAN = 'dipertimbangkan'
    DITOLAK = 'usulanditolak'
    DIGUGURKAN = 'digugurkan'
    SIFAT_KREASI_CHOICES = [
        (TERENCANA, 'Terencana'),
        (MODIFIKASI, 'Modifikasi'),
        (USULANBARU, 'Usulan Baru'),
        (DIPERTIMBANGKAN, 'Dipertimbangkan'),
        (DITOLAK, 'Usulan Ditolak'),
        (DIGUGURKAN, 'Digugurkan'),
    ]

    kode_program = models.CharField(max_length=100)
    nama_program = models.CharField(max_length=100)
    kode_akun = models.CharField(max_length=20)
    owner_program = models.ForeignKey(Unit, on_delete=models.CASCADE)
    jenis_input_output = models.CharField(
        max_length=3,
        choices=JENIS_INPUT_OUTPUT_CHOICES,
        default=OUT,
    )
    jenis_program = models.CharField(
        max_length=8,
        choices=JENIS_PROGRAM_CHOICES,
        default=NON_ASSET,
    )
    sifat_kreasi = models.CharField(
        max_length=15,  # length of the longest choice
        choices=SIFAT_KREASI_CHOICES,
        default=TERENCANA,
    )
    periode_anggaran = models.CharField(
        max_length=5,
        choices=PERIODE_CHOICES,
        default=PERIODE_BULAN,
    )
    sifat_periode_anggaran = models.CharField(
        max_length=9,
        choices=SIFAT_PERIODE_CHOICES,
        default=SIFAT_FIKS,
    )
    # anggaran_realisasi = models.DecimalField(max_digits=25, decimal_places=2, default=0.00)
    # anggaran_selisih = models.DecimalField(max_digits=25, decimal_places=2, default=0.00)
    keterangan = models.TextField(null=True, blank=True)
    tahun_anggaran = models.IntegerField(default=2024,
        validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    anggaran_januari = models.DecimalField(
        max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
    anggaran_februari = models.DecimalField(
        max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
    anggaran_maret = models.DecimalField(
        max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
    anggaran_april = models.DecimalField(
        max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
    anggaran_mei = models.DecimalField(
        max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
    anggaran_juni = models.DecimalField(
        max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
    anggaran_juli = models.DecimalField(
        max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
    anggaran_agustus = models.DecimalField(
        max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
    anggaran_september = models.DecimalField(
        max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
    anggaran_oktober = models.DecimalField(
        max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
    anggaran_november = models.DecimalField(
        max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
    anggaran_desember = models.DecimalField(
        max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)

    def __str__(self):
        return self.kode_program + ' ' + self.nama_program

# class AnggaranProgram(TimeStampedModel):
#     kode_program = models.ForeignKey(ProgramKerja, on_delete=models.CASCADE)
#     tahun_anggaran = models.IntegerField(
#         validators=[MinValueValidator(1000), MaxValueValidator(9999)])
#     anggaran_januari = models.DecimalField(
#         max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
#     anggaran_februari = models.DecimalField(
#         max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
#     anggaran_maret = models.DecimalField(
#         max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
#     anggaran_april = models.DecimalField(
#         max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
#     anggaran_mei = models.DecimalField(
#         max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
#     anggaran_juni = models.DecimalField(
#         max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
#     anggaran_juli = models.DecimalField(
#         max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
#     anggaran_agustus = models.DecimalField(
#         max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
#     anggaran_september = models.DecimalField(
#         max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
#     anggaran_oktober = models.DecimalField(
#         max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
#     anggaran_november = models.DecimalField(
#         max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)
#     anggaran_desember = models.DecimalField(
#         max_digits=25, decimal_places=2, default=0.00, blank=True, null=True)

#     def __str__(self):
#         return self.kode_program.nama_program + ' ' + self.tahun_anggaran