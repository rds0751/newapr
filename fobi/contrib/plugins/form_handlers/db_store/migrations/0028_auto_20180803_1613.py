# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-03 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fobi_contrib_plugins_form_handlers_db_store', '0027_auto_20180803_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedformdataentry',
            name='application_id',
            field=models.CharField(default='PrkfNHxxJt', max_length=6),
        ),
    ]
