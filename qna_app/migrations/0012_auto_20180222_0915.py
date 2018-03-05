# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        ('qna_app', '0011_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='user',
            field=annoying.fields.AutoOneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
