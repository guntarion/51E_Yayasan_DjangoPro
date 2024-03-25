from django.db import models
from yayasan.institusi.models import Institusi
from core.models import TimeStampedModel


class Entitas(TimeStampedModel):
    TIPE_ENTITAS_CHOICES = (
        ('individu', 'Individu'),
        ('institusi', 'Institusi'),
        ('vendor', 'Vendor'),
    )

    PENYEBUTAN_CHOICES = (
        ('', ''),
        ('pak', 'Pak'),
        ('bu', 'Bu'),
        ('sdr', 'Sdr'),
        ('ustadz', 'Ustadz'),
        ('ustadzah', 'Ustadzah'),
        ('pt', 'PT'),
        ('cv', 'CV'),
        ('perusahaan', 'Perusahaan'),
        ('usaha', 'Usaha'),
        ('institusi', 'Institusi'),
        ('komunitas', 'Komunitas'),
    )

    STATUS_JAMAAH_CHOICES = (
        ('jamaah_aktif', 'Jamaah Aktif'),
        ('jamaah_non_aktif', 'Jamaah Non Aktif'),
        ('non_jamaah', 'Non Jamaah'),
    )

    nama_entitas = models.CharField(max_length=200)
    panggilan_entitas = models.CharField(
        max_length=200,  blank=True, null=True)
    tipe_entitas = models.CharField(
        max_length=10, choices=TIPE_ENTITAS_CHOICES)
    penyebutan = models.CharField(
        max_length=200, choices=PENYEBUTAN_CHOICES,  blank=True, null=True, default='')
    status_jamaah = models.CharField(
        max_length=200, choices=STATUS_JAMAAH_CHOICES, blank=True, null=True)
    organisasi = models.ForeignKey(Institusi, on_delete=models.CASCADE)
    alamat = models.TextField(blank=True, null=True)
    wilayah_domisili = models.CharField(max_length=200, blank=True, null=True)
    kota_domisili = models.CharField(max_length=200, blank=True, null=True)
    nomor_whatsapp = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)  # Hanya untuk organisasi
    is_panitia = models.BooleanField(default=False)
    is_donatur = models.BooleanField(default=False)
    is_internal = models.BooleanField(default=False)
    id_kencleng = models.CharField(max_length=10, blank=True, null=True)
    id_tunai = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.nama_entitas


# class Vendor(TimeStampedModel):
#     nama_vendor = models.CharField(max_length=200)
#     jenis_entitas = models.CharField(max_length=200)
#     bidang_usaha = models.CharField(max_length=200)
#     alamat = models.TextField()
#     kota_kantor = models.CharField(max_length=200)
#     status = models.CharField(max_length=200)
#     keterangan = models.TextField()
#     organisasi = models.ForeignKey(Institusi, on_delete=models.CASCADE)
#     nomor_whatsapp = models.CharField(max_length=15)
#     email = models.EmailField(blank=True, null=True)  # Opsional
#     website = models.URLField(blank=True, null=True)  # Hanya untuk organisasi

#     def __str__(self):
#         return self.nama_vendor
