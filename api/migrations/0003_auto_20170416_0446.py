# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_section_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='name',
            field=models.CharField(blank=True, default=None, help_text='Only visible to you. Use it to manage yours sections', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='page',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='sections', to='api.Page'),
        ),
    ]