# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-07-26 05:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fobi_contrib_plugins_form_handlers_db_store', '0016_auto_20180726_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedformdataentry',
            name='application_id',
            field=models.CharField(default='dzTqAEEQKT', max_length=6),
        ),
    ]
