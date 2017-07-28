# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-27 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoextended',
            name='imageGallery',
            field=models.BooleanField(default=False, help_text='Decide whether or not this image will be shown in the gallery', verbose_name='Gallery'),
        ),
        migrations.AddField(
            model_name='photoextended',
            name='indexPageCarousel',
            field=models.BooleanField(default=False, help_text='Decide whether or not this image will be included in the Home Page Carousel', verbose_name='Carousel'),
        ),
    ]
