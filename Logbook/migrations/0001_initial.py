# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centre_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Climb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('climb_colour', models.CharField(max_length=250)),
                ('climb_grade', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Climber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('climber_name', models.CharField(max_length=100)),
                ('climber_age', models.IntegerField()),
            ],
        ),
    ]
