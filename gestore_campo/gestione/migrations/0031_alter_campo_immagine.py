# Generated by Django 4.0.5 on 2022-06-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0030_alter_prenotazione_options_alter_campo_immagine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campo',
            name='immagine',
            field=models.ImageField(default='static/img/logo.jpg', upload_to='campo'),
        ),
    ]