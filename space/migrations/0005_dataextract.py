# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-23 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0004_auto_20160423_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataExtract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
