# Generated by Django 4.0.4 on 2022-06-10 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0011_rename_giorni_ora_giorno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giorno',
            name='giorno',
            field=models.CharField(choices=[('Lunedi', 'Lunedi'), ('Lunedi', 'Martedi'), ('Lunedi', 'Mercoledi'), ('Lunedi', 'Giovedi'), ('Lunedi', 'Venerdi'), ('Lunedi', 'Sabato'), ('Lunedi', 'Domenica')], max_length=100),
        ),
    ]
