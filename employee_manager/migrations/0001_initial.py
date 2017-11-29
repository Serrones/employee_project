# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('department', models.CharField(max_length=30, unique=True, verbose_name='Departamento')),
            ],
        ),
    ]
