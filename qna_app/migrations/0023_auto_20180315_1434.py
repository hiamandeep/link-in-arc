# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-15 09:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qna_app', '0022_totalproblem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='current_level',
            new_name='current_problem',
        ),
    ]