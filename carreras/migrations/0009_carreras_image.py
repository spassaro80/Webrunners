# Generated by Django 2.2.5 on 2019-11-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0008_auto_20191121_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='carreras',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projects', verbose_name='Imagen'),
        ),
    ]
