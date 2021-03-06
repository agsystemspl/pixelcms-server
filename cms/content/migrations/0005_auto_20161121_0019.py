# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 23:19
from __future__ import unicode_literals

import cms.common.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_category_image_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoriesmodule',
            name='categories_names_headers_level',
        ),
        migrations.RemoveField(
            model_name='categoriesmodule',
            name='show_categories_descriptions',
        ),
        migrations.RemoveField(
            model_name='categoriesmodule',
            name='show_categories_names',
        ),
        migrations.AddField(
            model_name='categoriesmodule',
            name='images_size',
            field=cms.common.fields.FilebrowserVersionField(choices=[('1col', '1 column (65x37)'), ('2cols', '2 columns (160x90)'), ('3cols', '3 columns (255x143)'), ('4cols', '4 columns (350x197)'), ('5cols', '5 columns (445x250)'), ('6cols', '6 columns (540x304)'), ('7cols', '7 columns (635x357)'), ('8cols', '8 columns (730x411)'), ('9cols', '9 columns (825x464)'), ('10cols', '10 columns (920x518)'), ('11cols', '11 columns (1015x571)'), ('12cols', '12 columns (1110x624)'), ('fullhd', 'Full HD (1920x1080)')], default='3cols', max_length=255, verbose_name='images size'),
        ),
        migrations.AddField(
            model_name='categoriesmodule',
            name='names_headers_level',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='3', max_length=1, verbose_name='names headers level'),
        ),
        migrations.AddField(
            model_name='categoriesmodule',
            name='show_descriptions',
            field=models.BooleanField(default=True, verbose_name='show descriptions'),
        ),
        migrations.AddField(
            model_name='categoriesmodule',
            name='show_images',
            field=models.BooleanField(default=True, verbose_name='show images'),
        ),
        migrations.AddField(
            model_name='categoriesmodule',
            name='show_names',
            field=models.BooleanField(default=True, verbose_name='show names'),
        ),
    ]
