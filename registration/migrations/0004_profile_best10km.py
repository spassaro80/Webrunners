# Generated by Django 2.2.5 on 2020-04-08 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20200114_0634'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='best10km',
            field=models.TimeField(null=True, verbose_name='Mejor marca 10km'),
        ),
    ]