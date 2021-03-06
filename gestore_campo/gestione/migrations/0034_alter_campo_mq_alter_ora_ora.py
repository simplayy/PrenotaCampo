# Generated by Django 4.0.5 on 2022-07-05 14:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0033_alter_campo_immagine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campo',
            name='mq',
            field=models.IntegerField(default=800),
        ),
        migrations.AlterField(
            model_name='ora',
            name='ora',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(24), django.core.validators.MinValueValidator(0)]),
        ),
    ]
