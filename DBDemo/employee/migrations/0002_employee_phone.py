# Generated by Django 3.0.6 on 2020-06-04 05:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.BigIntegerField(default=0, validators=[django.core.validators.MinValueValidator(6666666666, 'Invalid Phone Number'), django.core.validators.MaxValueValidator(9999999999, 'Invalid Phone Number')], verbose_name='Phone'),
        ),
    ]