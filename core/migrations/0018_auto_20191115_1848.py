# Generated by Django 2.2.5 on 2019-11-15 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_equipo_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='color',
            field=models.CharField(max_length=100, verbose_name='Color'),
        ),
    ]
