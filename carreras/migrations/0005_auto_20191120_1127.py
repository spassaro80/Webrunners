# Generated by Django 2.2.5 on 2019-11-20 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0004_auto_20191120_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
    ]