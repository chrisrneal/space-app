# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-23 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0002_auto_20160423_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='symptom',
            name='city',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='symptom',
            name='country',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='symptom',
            name='postal',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='symptom',
            name='province',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
