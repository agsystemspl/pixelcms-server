# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-31 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='site_name',
            field=models.CharField(blank=True, default='PixelCMS site', max_length=255, verbose_name='site name'),
        ),
    ]
