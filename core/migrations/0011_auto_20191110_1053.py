# Generated by Django 2.2.5 on 2019-11-10 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_individual'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carreras',
            name='number',
        ),
        migrations.RemoveField(
            model_name='carreras',
            name='runners',
        ),
    ]
