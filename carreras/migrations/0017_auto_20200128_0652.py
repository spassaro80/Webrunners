# Generated by Django 2.2.5 on 2020-01-28 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0016_runners_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runners',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]