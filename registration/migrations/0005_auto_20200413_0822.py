# Generated by Django 2.2.5 on 2020-04-13 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_profile_best10km'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='best21km',
            field=models.TimeField(null=True, verbose_name='Mejor marca 21km'),
        ),
        migrations.AddField(
            model_name='profile',
            name='best42km',
            field=models.TimeField(null=True, verbose_name='Mejor marca 42km'),
        ),
    ]