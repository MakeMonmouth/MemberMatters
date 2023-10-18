# Generated by Django 3.2.20 on 2023-10-09 14:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("access", "0012_auto_20231009_2222"),
    ]

    def set_current_devices_authorised(apps, schema_editor):
        DeviceModels = [
            apps.get_model("access", "MemberbucksDevice"),
            apps.get_model("access", "Doors"),
            apps.get_model("access", "Interlock"),
        ]
        for DeviceClass in DeviceModels:
            for device in DeviceClass.objects.all():
                device.authorised = True
                device.save()
                print()
                print(f"Updated {device.name} to be authorised")

    operations = [
        migrations.AddField(
            model_name="accesscontrolleddevice",
            name="authorised",
            field=models.BooleanField(
                default=False,
                verbose_name="Is this device authorised to access the system?",
            ),
        ),
        migrations.RunPython(set_current_devices_authorised),
    ]