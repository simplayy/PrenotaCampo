# Generated by Django 4.0.5 on 2022-06-18 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0016_prenotazione'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giorno',
            name='giorno',
            field=models.SmallIntegerField(choices=[(0, 'Lunedi'), (1, 'Martedi'), (2, 'Mercoledi'), (3, 'Giovedi'), (4, 'Venerdi'), (5, 'Sabato'), (6, 'Domenica')]),
        ),
    ]