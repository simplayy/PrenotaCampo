# Generated by Django 4.0.4 on 2022-06-10 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0007_campo_utente'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='giorno',
            unique_together={('giorno', 'campo')},
        ),
    ]
