# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 20:16
from __future__ import unicode_literals

import autoslug.fields
import cms.common.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('published', models.BooleanField(default=True, verbose_name='published')),
                ('template_id', autoslug.fields.AutoSlugField(blank=True, editable=True, populate_from='name', unique_with=('language',), verbose_name='template id')),
                ('show_module_name', models.BooleanField(default=True, verbose_name='show module name')),
                ('module_name_header_level', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='2', max_length=1, verbose_name='module name header level')),
                ('html_class', models.CharField(blank=True, default='', max_length=255, verbose_name='HTML class')),
                ('language', cms.common.fields.LanguageField(choices=[('any', '(any)'), ('pl', 'Polish')], default='any', max_length=5, verbose_name='language')),
                ('show_categories_names', models.BooleanField(default=True, verbose_name='show categories names')),
                ('categories_names_headers_level', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='3', max_length=1, verbose_name='categories names headers level')),
                ('show_categories_descriptions', models.BooleanField(default=True, verbose_name='show categories descriptions')),
            ],
            options={
                'verbose_name_plural': 'categories modules',
                'verbose_name': 'categories module',
                'ordering': ('language', 'name'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CategoriesModuleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='order')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Category')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.CategoriesModule')),
            ],
            options={
                'verbose_name_plural': 'categories',
                'verbose_name': 'category',
                'ordering': ('order',),
            },
        ),
        migrations.AddField(
            model_name='categoriesmodule',
            name='categories',
            field=models.ManyToManyField(blank=True, through='content.CategoriesModuleCategory', to='content.Category'),
        ),
    ]
