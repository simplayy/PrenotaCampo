# Generated by Django 4.0.5 on 2022-06-26 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0028_campo_rates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campo',
            name='rates',
        ),
    ]