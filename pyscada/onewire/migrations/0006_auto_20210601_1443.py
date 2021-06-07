# Generated by Django 2.2.8 on 2021-06-01 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onewire', '0005_extendedonewiredevice_extendedonewirevariable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onewirevariable',
            name='sensor_type',
            field=models.CharField(choices=[('DS18B20', 'DS18B20 Temperature Sensor')], default='DS18B20', max_length=10),
        ),
    ]
