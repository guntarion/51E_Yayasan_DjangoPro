# Generated by Django 4.2.9 on 2024-03-22 06:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnggaranProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tahun_anggaran', models.IntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)])),
                ('anggaran_setahun', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=25, null=True)),
                ('anggaran_januari', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=25, null=True)),
                ('anggaran_februari', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=25, null=True)),
                ('anggaran_maret', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=25, null=True)),
                ('anggaran_april', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=25, null=True)),
                ('anggaran_mei', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=25, null=True)),
                ('anggaran_juni', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=25, null=True)),
                ('anggaran_juli', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=25, null=True)),
                ('anggaran_agustus', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=25, null=True)),
                ('anggaran_september', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=25, null=True)),
                ('anggaran_oktober', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=25, null=True)),
                ('anggaran_november', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=25, null=True)),
                ('anggaran_desember', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=25, null=True)),
                ('kode_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.programkerja')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
