# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-01 08:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fobi_contrib_plugins_form_handlers_db_store', '0021_auto_20180726_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedformdataentry',
            name='application_id',
            field=models.CharField(default='FKXQVYAhaf', max_length=6),
        ),
        migrations.AlterField(
            model_name='savedformdataentry',
            name='approved_by',
            field=models.ManyToManyField(blank=True, related_name='approved_by', to=settings.AUTH_USER_MODEL, verbose_name='approvers'),
        ),
        migrations.AlterField(
            model_name='savedformdataentry',
            name='disapproved_by',
            field=models.ManyToManyField(blank=True, related_name='disapproved_by', to=settings.AUTH_USER_MODEL, verbose_name='disapprovers'),
        ),
    ]
