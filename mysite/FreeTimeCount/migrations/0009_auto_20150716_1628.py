# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FreeTimeCount', '0008_course_course_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursetable',
            name='course',
        ),
        migrations.AddField(
            model_name='coursetable',
            name='course_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
