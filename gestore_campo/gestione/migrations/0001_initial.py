# Generated by Django 4.0.4 on 2022-05-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indirizzo', models.CharField(max_length=200)),
                ('prezzo', models.FloatField(max_length=50)),
                ('mq', models.IntegerField(default=100)),
            ],
        ),
    ]
