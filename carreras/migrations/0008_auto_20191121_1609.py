# Generated by Django 2.2.5 on 2019-11-21 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0007_auto_20191121_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='name',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='carreras.carreras', verbose_name='Nombre'),
        ),
    ]
