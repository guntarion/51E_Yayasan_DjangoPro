from django.db import models

# Create your models here.
class Institusi(models.Model):
    nama_institusi = models.CharField(max_length=200)
    julukan_institusi = models.CharField(max_length=50)
    alamat = models.TextField()
    wilayah = models.CharField(max_length=200)
    kota = models.CharField(max_length=200)
    nomorWA = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nama_institusi

class Bidang(models.Model):
    namaBidang = models.CharField(max_length=200)
    kodeBidang = models.CharField(max_length=10, null=True)
    organisasi = models.ForeignKey(Institusi, on_delete=models.CASCADE)

    def __str__(self):
        return self.namaBidang
    
class Unit(models.Model):
    namaUnit = models.CharField(max_length=200)
    kodeUnit = models.CharField(max_length=10)
    bidang = models.ForeignKey(Bidang, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.namaUnit)
        # return self.kodeUnit + ' ' + self.namaUnit
