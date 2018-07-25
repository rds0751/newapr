# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-07-22 21:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('lastchanged', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('lastchanged', models.DateTimeField(auto_now=True)),
                ('alert', models.BooleanField(default=False, help_text='Check this if you want to be alerted when a new response is added.', verbose_name='Alert')),
                ('name', models.CharField(blank=True, help_text='Enter your first and last name.', max_length=64, null=True, verbose_name='Name')),
                ('email', models.EmailField(blank=True, help_text='Enter a valid email address.', max_length=254, null=True, verbose_name='Email')),
                ('title', models.CharField(help_text='Enter your question or suggestion.', max_length=255, verbose_name='Question')),
                ('body', models.TextField(blank=True, help_text='Please offer details. Markdown enabled.', null=True, verbose_name='Description')),
                ('status', models.CharField(choices=[('public', 'Public'), ('private', 'Private'), ('internal', 'Internal')], db_index=True, default='private', max_length=32, verbose_name='Status')),
                ('locked', models.BooleanField(default=False)),
                ('categories', models.ManyToManyField(blank=True, to='knowledge.Category')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ['-added'],
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('lastchanged', models.DateTimeField(auto_now=True)),
                ('alert', models.BooleanField(default=False, help_text='Check this if you want to be alerted when a new response is added.', verbose_name='Alert')),
                ('name', models.CharField(blank=True, help_text='Enter your first and last name.', max_length=64, null=True, verbose_name='Name')),
                ('email', models.EmailField(blank=True, help_text='Enter a valid email address.', max_length=254, null=True, verbose_name='Email')),
                ('body', models.TextField(blank=True, help_text='Please enter your response. Markdown enabled.', null=True, verbose_name='Response')),
                ('status', models.CharField(choices=[('public', 'Public'), ('private', 'Private'), ('internal', 'Internal'), ('inherit', 'Inherit')], db_index=True, default='inherit', max_length=32, verbose_name='Status')),
                ('accepted', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='knowledge.Question')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Response',
                'verbose_name_plural': 'Responses',
                'ordering': ['added'],
            },
        ),
    ]
