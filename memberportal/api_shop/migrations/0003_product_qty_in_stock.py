# Generated by Django 3.2.22 on 2023-11-18 20:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api_shop", "0002_auto_20231119_0615"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="qty_in_stock",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
