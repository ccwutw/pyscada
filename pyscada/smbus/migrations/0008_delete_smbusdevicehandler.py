# Generated by Django 2.2.8 on 2021-06-01 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smbus', '0007_remove_smbusdevice_instrument'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SMBusDeviceHandler',
        ),
    ]
