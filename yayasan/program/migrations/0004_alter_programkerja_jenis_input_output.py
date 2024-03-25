# Generated by Django 4.2.9 on 2024-03-22 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0003_alter_programkerja_keterangan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programkerja',
            name='jenis_input_output',
            field=models.CharField(choices=[('TER', 'Input Terikat'), ('BEB', 'Input Bebas'), ('OUT', 'Output')], default='OUT', max_length=3),
        ),
    ]
