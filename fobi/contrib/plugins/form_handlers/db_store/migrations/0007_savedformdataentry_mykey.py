# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-14 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fobi_contrib_plugins_form_handlers_db_store', '0006_savedformdataentry_submitted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedformdataentry',
            name='mykey',
            field=models.CharField(default='4F5JCzRXJu', max_length=6, null=True),
        ),
    ]