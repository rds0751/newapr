# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-05 18:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oname', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='oid',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.Organization'),
        ),
    ]
