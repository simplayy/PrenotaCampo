# Generated by Django 4.0.5 on 2022-06-28 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione', '0032_alter_campo_immagine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campo',
            name='immagine',
            field=models.ImageField(default='campo/default.jpg', upload_to='campo'),
        ),
    ]