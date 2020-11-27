# Generated by Django 3.0.6 on 2020-06-04 05:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3, 'Name should be 3 chars long'), django.core.validators.MaxLengthValidator(50, 'Name shoild not be longer than 50 chars')], verbose_name='Name')),
                ('email', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(5, 'Name should be 5 chars long'), django.core.validators.MaxLengthValidator(50, 'Name shoild not be longer than 50 chars'), django.core.validators.EmailValidator('Invalid Email')], verbose_name='Email')),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(20, 'Age should be above 20'), django.core.validators.MaxValueValidator(70, 'Age should be below 70')], verbose_name='Age')),
                ('role', models.CharField(choices=[('Senior Developer', 'Senior Developer'), ('Junior Developer', 'Junior Developer'), ('Software Tester', 'Software Tester')], max_length=100, verbose_name='Role')),
            ],
        ),
    ]
