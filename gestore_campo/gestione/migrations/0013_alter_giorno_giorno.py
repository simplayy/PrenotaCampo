# Generated by Django 4.0.4 on 2022-06-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0012_alter_giorno_giorno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giorno',
            name='giorno',
            field=models.CharField(choices=[('Lunedi', 'Lunedi'), ('Martedi', 'Martedi'), ('Mercoledi', 'Mercoledi'), ('Giovedi', 'Giovedi'), ('Venerdi', 'Venerdi'), ('Sabato', 'Sabato'), ('Domenica', 'Domenica')], max_length=100),
        ),
    ]