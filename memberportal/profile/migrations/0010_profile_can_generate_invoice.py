# Generated by Django 2.0.9 on 2018-12-26 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0009_auto_20181204_0417'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='can_generate_invoice',
            field=models.BooleanField(default=False, verbose_name='Can generate & email invoice'),
        ),
    ]