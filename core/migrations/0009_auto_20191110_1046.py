# Generated by Django 2.2.5 on 2019-11-10 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20191110_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carreras',
            name='runners',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.runners'),
        ),
    ]