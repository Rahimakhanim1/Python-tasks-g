# Generated by Django 5.0 on 2024-01-03 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinif',
            name='sagird_yasi',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sinifadres',
            name='sinif',
            field=models.IntegerField(),
        ),
    ]
