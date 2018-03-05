# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qna_app', '0009_auto_20180208_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='level',
            field=models.IntegerField(null=True),
        ),
    ]
