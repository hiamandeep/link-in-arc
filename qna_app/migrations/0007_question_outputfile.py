# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qna_app', '0006_question_inputfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='outputfile',
            field=models.FileField(default='def_out', upload_to='output_files/'),
        ),
    ]
