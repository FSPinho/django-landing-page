# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 19:31
from __future__ import unicode_literals

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20170413_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagelink',
            name='color',
            field=models.CharField(choices=[('primary', 'Primary color'), ('accent', 'Accent color')], default='primary', max_length=255),
        ),
        migrations.AddField(
            model_name='pagelink',
            name='order',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sociallink',
            name='color',
            field=models.CharField(choices=[('primary', 'Primary color'), ('accent', 'Accent color')], default='primary', max_length=255),
        ),
        migrations.AddField(
            model_name='toolbarlink',
            name='color',
            field=models.CharField(choices=[('primary', 'Primary color'), ('accent', 'Accent color')], default='primary', max_length=255),
        ),
        migrations.AlterField(
            model_name='pagelink',
            name='icon',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default=None, null=True, upload_to='uploads/icons'),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='icon',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default=None, null=True, upload_to='uploads/icons'),
        ),
        migrations.AlterField(
            model_name='toolbarlink',
            name='icon',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default=None, null=True, upload_to='uploads/icons'),
        ),
    ]
