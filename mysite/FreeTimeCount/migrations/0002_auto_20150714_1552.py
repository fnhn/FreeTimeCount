# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FreeTimeCount', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursetable',
            name='course_id',
        ),
        migrations.RemoveField(
            model_name='coursetable',
            name='stu_id',
        ),
        migrations.AddField(
            model_name='coursetable',
            name='course',
            field=models.ForeignKey(default=0, to='FreeTimeCount.Course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursetable',
            name='member',
            field=models.ForeignKey(default=0, to='FreeTimeCount.Member'),
            preserve_default=False,
        ),
    ]
