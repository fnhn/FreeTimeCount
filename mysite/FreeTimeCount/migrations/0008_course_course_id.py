# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FreeTimeCount', '0007_auto_20150715_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
