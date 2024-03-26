from django.db import models


class Student(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    LIVING_WITH_CHOICES = [('ortu', 'Bersama orang tua'),
                           ('wali', 'Bersama wali')]
    TRANSPORTATION_CHOICES = [
        ('sepedamotor', 'Sepeda motor'), ('mobil', 'Mobil pribadi'), ('jalan', 'Jalan kaki')]

    name = models.CharField(max_length=100)
    nipd = models.CharField(max_length=20)
    nisn = models.CharField(max_length=20)
    nik = models.CharField(max_length=16)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_place = models.CharField(max_length=50)
    birth_date = models.DateField()
    religion = models.CharField(max_length=30, default='Islam')
    address = models.TextField()
    rt = models.CharField(max_length=3)
    rw = models.CharField(max_length=3)
    village = models.CharField(max_length=50)
    sub_district = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)
    living_with = models.CharField(max_length=10, choices=LIVING_WITH_CHOICES)
    transportation = models.CharField(
        max_length=20, choices=TRANSPORTATION_CHOICES)
    current_class = models.CharField(max_length=50)
    national_exam_number = models.CharField(max_length=20)
    diploma_number = models.CharField(max_length=20)
    birth_certificate_number = models.CharField(max_length=20)
    bank = models.CharField(max_length=50)
    bank_account_number = models.CharField(max_length=20)
    account_holder_name = models.CharField(max_length=100)
    previous_school = models.CharField(max_length=100)
    child_order = models.IntegerField()
    family_card_number = models.CharField(max_length=20)
    weight = models.IntegerField()
    height = models.IntegerField()
    head_circumference = models.IntegerField()
    siblings_count = models.IntegerField()
    distance_to_school = models.FloatField()

    def __str__(self):
        return self.name

class Parent(models.Model):
    EDUCATION_LEVEL_CHOICES = [
        ('noschooling', 'Tidak sekolah'),
        ('smp', 'SMP/sederajat'),
        ('sma', 'SMA/sederajat'),
        ('diploma', 'D3'),
        ('sarjana', 'S1'),
        ('master', 'S2'),
        ('doktor', 'S3'),
    ]
    JOB_CHOICES = [
        ('swasta', 'Karyawan Swasta'),
        ('tentara', 'TNI/Polri'),
        ('pengusaha', 'Wiraswasta'),
        ('lainnya', 'Lainnya'),
        ('pns', 'Karyawan BUMN'),
    ]
    INCOME_CHOICES = [
        ('<2M', 'kurang dari Rp. 2,000,000'),
        ('2M-5M', 'Rp. 2,000,000 - Rp. 4,999,999'),
        ('5M-20M', 'Rp. 5,000,000 - Rp. 20,000,000'),
        ('>20M', 'di atas Rp. 20,000,000'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField()
    education_level = models.CharField(max_length=20, choices=EDUCATION_LEVEL_CHOICES)
    job = models.CharField(max_length=50, choices=JOB_CHOICES)
    income = models.CharField(max_length=6, choices=INCOME_CHOICES)
    nik = models.CharField(max_length=16)

    def __str__(self):
        return self.name
    
class Payment(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('PMB', 'Biaya Penerimaan Murid Baru'),
        ('DUL', 'Biaya Daftar Ulang'),
        ('SPP', 'Sumbangan Pembinaan Pendidikan')
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    receipt_number = models.CharField(max_length=50)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_type = models.CharField(max_length=3, choices=PAYMENT_TYPE_CHOICES)
    class_name = models.CharField(max_length=50)
    # Untuk SPP, perlu menambahkan field untuk bulan dan tahun pembayaran
    month = models.IntegerField(null=True, blank=True)  # Bulan untuk pembayaran SPP
    year = models.IntegerField(null=True, blank=True)   # Tahun untuk pembayaran SPP

    def __str__(self):
        return f"{self.get_payment_type_display()} - {self.student.name}"


class InstallmentPayment(models.Model):
    #  Model ini akan membantu mencatat setiap angsuran yang dibuat untuk pembayaran PMB dan DU.
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='installments')
    installment_date = models.DateField()
    installment_amount = models.DecimalField(max_digits=12, decimal_places=2)
    remaining_amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Installment for {self.payment.student.name} on {self.installment_date}"
