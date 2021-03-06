# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 21:11
from __future__ import unicode_literals

import cms.common.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', cms.common.fields.LanguageField(choices=[('any', '(any)'), ('en', 'English')], default='any', max_length=5, unique=True, verbose_name='language')),
                ('site_name', models.CharField(max_length=255, verbose_name='site name')),
                ('page_title_site_name_suffix', models.BooleanField(default=True, verbose_name='site name suffix in page title')),
                ('suffix_separator', models.CharField(default='|', max_length=10, verbose_name='suffix separator')),
                ('meta_description', models.CharField(blank=True, default='', max_length=255, verbose_name='description')),
                ('meta_robots', models.CharField(blank=True, default='index, follow', max_length=255, verbose_name='robots')),
            ],
            options={
                'verbose_name_plural': 'general settings',
                'verbose_name': 'general settings',
                'ordering': ('language',),
            },
        ),
    ]
