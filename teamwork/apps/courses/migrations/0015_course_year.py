# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 01:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20170228_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='year',
            field=models.CharField(default=2017, max_length=20),
        ),
    ]