# Generated by Django 4.0.4 on 2022-06-10 09:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestione', '0008_alter_giorno_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='campo',
            unique_together={('utente', 'id')},
        ),
    ]