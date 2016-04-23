# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-23 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='symptom',
            name='streetaddress',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='symptom',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
