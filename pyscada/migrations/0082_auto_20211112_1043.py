# Generated by Django 2.2.24 on 2021-11-12 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyscada', '0081_calculatedvariable_periodfield_variablecalculatedfields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodfield',
            name='property',
            field=models.CharField(blank=True, default='', help_text='used for count value for exemple', max_length=255, null=True),
        ),
    ]