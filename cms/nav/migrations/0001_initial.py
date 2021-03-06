# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 21:11
from __future__ import unicode_literals

import autoslug.fields
import cms.common.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NavModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('published', models.BooleanField(default=True, verbose_name='published')),
                ('template_id', autoslug.fields.AutoSlugField(blank=True, editable=True, populate_from='name', unique_with=('language',), verbose_name='template id')),
                ('show_module_name', models.BooleanField(default=True, verbose_name='show module name')),
                ('module_name_header_level', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='2', max_length=1, verbose_name='module name header level')),
                ('html_class', models.CharField(blank=True, default='', max_length=255, verbose_name='HTML class')),
                ('language', cms.common.fields.LanguageField(choices=[('any', '(any)'), ('en', 'English')], default='any', max_length=5, verbose_name='language')),
            ],
            options={
                'verbose_name_plural': 'nav modules',
                'verbose_name': 'nav module',
                'ordering': ('language', 'name'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NavModuleItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Overrides <strong>Page</strong> title. Required when nav scrolls to element or is link.', max_length=255, null=True, verbose_name='name')),
                ('scroll_to_element', models.CharField(blank=True, default='', help_text='HTML id of element on page. Overrides <strong>Page</strong>.', max_length=255, verbose_name='scroll to element')),
                ('link', models.CharField(blank=True, default='', help_text='Overrides <strong>Page</strong> and <strong>Scroll to element</strong>.', max_length=255, verbose_name='link')),
                ('link_open_in_new_tab', models.BooleanField(default=False, verbose_name='open link in new tab')),
                ('published', models.BooleanField(default=True, verbose_name='published')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='order')),
                ('nav', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='nav.NavModule', verbose_name='nav')),
            ],
            options={
                'verbose_name_plural': 'items',
                'verbose_name': 'item',
                'ordering': ('order',),
            },
        ),
    ]
