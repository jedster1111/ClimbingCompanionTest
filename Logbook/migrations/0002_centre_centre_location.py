# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Logbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='centre',
            name='centre_location',
            field=models.CharField(default='Lancaster', max_length=500),
            preserve_default=False,
        ),
    ]
