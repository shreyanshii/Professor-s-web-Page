# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-11 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='Department',
            field=models.CharField(choices=[('CSE', 'CSE'), ('MC', 'MC')], default='CSE', max_length=100),
        ),
        migrations.AlterField(
            model_name='info',
            name='Name',
            field=models.CharField(help_text='Enter Name', max_length=250),
        ),
    ]
