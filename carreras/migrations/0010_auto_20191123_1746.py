# Generated by Django 2.2.5 on 2019-11-23 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0009_carreras_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carreras',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='carreras', verbose_name='Imagen'),
        ),
    ]
