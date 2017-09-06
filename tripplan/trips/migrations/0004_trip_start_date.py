# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_auto_20170829_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]