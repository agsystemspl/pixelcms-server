# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='subject')),
                ('recipients', models.TextField(verbose_name='recipients')),
                ('content', models.TextField(verbose_name='content')),
                ('reply_to', models.CharField(max_length=255, verbose_name='reply to')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('sent', models.BooleanField(default=False, verbose_name='sent')),
                ('postdate', models.DateTimeField(blank=True, null=True, verbose_name='postdate')),
            ],
            options={
                'verbose_name_plural': 'messages',
                'verbose_name': 'message',
                'ordering': ('-created',),
            },
        ),
    ]
