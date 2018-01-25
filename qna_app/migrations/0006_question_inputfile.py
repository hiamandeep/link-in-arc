# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qna_app', '0005_question_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='inputfile',
            field=models.FileField(default='def_in', upload_to='input_files/'),
        ),
    ]
