# Generated by Django 2.2.5 on 2019-11-20 09:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carreras',
            name='created',
            field=models.DateField(default=datetime.datetime(2019, 11, 20, 9, 51, 15, 883527, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='carreras',
            name='description',
            field=models.TextField(default='descripción'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carreras',
            name='modified',
            field=models.DateField(default=datetime.datetime(2019, 11, 20, 9, 51, 15, 883527, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='carreras',
            name='urlfield',
            field=models.URLField(blank=True, null=True, verbose_name='Resultados'),
        ),
    ]
