# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-09 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180706_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='oid',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
    ]
