# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170413_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='alias',
            field=models.SlugField(default='', help_text='Will be as the page URL', max_length=32, unique=True),
        ),
    ]