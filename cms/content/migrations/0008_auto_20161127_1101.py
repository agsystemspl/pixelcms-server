# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 10:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20161127_1100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='show_article_contents',
            new_name='show_articles_contents',
        ),
    ]
