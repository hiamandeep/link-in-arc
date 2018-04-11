# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-14 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna_app', '0019_auto_20180304_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='accuracy',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='numuser',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='wrong',
            field=models.IntegerField(default=0),
        ),
    ]