# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-23 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0003_auto_20160423_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptom',
            name='locLat',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='symptom',
            name='locLong',
            field=models.FloatField(blank=True),
        ),
    ]
