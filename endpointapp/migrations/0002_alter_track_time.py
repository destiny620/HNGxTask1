# Generated by Django 4.2.5 on 2023-09-08 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpointapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='time',
            field=models.DateTimeField(verbose_name='2023-09-08T22:52:29Z'),
        ),
    ]
