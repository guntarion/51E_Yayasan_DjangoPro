# Generated by Django 4.2.9 on 2024-03-24 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entitas', '0003_entitas_id_kencleng_entitas_id_tunai_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entitas',
            name='alamat',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entitas',
            name='kota_domisili',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='entitas',
            name='nomor_whatsapp',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='entitas',
            name='panggilan_entitas',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='entitas',
            name='penyebutan',
            field=models.CharField(blank=True, choices=[('', ''), ('bapak', 'Bapak'), ('ibu', 'Ibu'), ('mas', 'Mas'), ('mbak', 'Mbak'), ('ustadz', 'Ustadz'), ('ustadzah', 'Ustadzah'), ('pt', 'PT'), ('cv', 'CV'), ('perusahaan', 'Perusahaan'), ('usaha', 'Usaha'), ('komunitas', 'Komunitas')], default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='entitas',
            name='wilayah_domisili',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]