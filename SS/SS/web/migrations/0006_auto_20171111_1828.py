# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-11 12:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='end',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start',
        ),
    ]
