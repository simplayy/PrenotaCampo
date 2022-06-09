# Generated by Django 4.0.4 on 2022-06-09 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0005_giorno_ora_delete_prenotazione_giorno_ore_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campo',
            name='giorni',
        ),
        migrations.RemoveField(
            model_name='giorno',
            name='ore',
        ),
        migrations.AddField(
            model_name='giorno',
            name='campo',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestione.campo'),
        ),
        migrations.AddField(
            model_name='ora',
            name='giorni',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestione.giorno'),
        ),
    ]
