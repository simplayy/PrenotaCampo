# Generated by Django 4.0.4 on 2022-06-10 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0009_alter_campo_id_alter_campo_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='campo',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='giorno',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='campo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]