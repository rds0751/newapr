# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-07-25 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fobi_contrib_plugins_form_handlers_db_store', '0014_merge_20180725_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='ident',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='savedformdataentry',
            name='application_id',
            field=models.CharField(default='R3A9LG4XBH', max_length=6),
        ),
    ]
