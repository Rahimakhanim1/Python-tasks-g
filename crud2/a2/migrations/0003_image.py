# Generated by Django 5.0 on 2023-12-25 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a2', '0002_table_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='images/')),
            ],
        ),
    ]
