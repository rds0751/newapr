# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-08 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='doc',
            field=models.FileField(blank=True, upload_to='sent_docs/'),
        ),
    ]
