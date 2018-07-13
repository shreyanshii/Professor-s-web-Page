# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 11:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Degree', models.CharField(max_length=25)),
                ('College_Name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Designation', models.CharField(max_length=300)),
                ('Phone', models.CharField(max_length=20)),
                ('webmail', models.CharField(max_length=100)),
                ('office', models.CharField(max_length=100)),
                ('residence', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Position', models.CharField(max_length=200)),
                ('Place', models.CharField(max_length=200)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Info')),
            ],
        ),
        migrations.AddField(
            model_name='education',
            name='info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Info'),
        ),
    ]
