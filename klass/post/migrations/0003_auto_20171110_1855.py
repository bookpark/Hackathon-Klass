# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20171110_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='context',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]