# Generated by Django 2.2.8 on 2020-09-18 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmi', '0031_auto_20200918_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='displayvalueoption',
            name='color_level_1',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='displayvalueoption',
            name='color_level_2',
            field=models.FloatField(default=50, help_text='Only needed for 3 colors and gradient'),
        ),
    ]