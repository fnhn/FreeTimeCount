# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FreeTimeCount', '0009_auto_20150716_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='member',
            name='department',
        ),
        migrations.RemoveField(
            model_name='member',
            name='dormitory',
        ),
        migrations.RemoveField(
            model_name='member',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='member',
            name='is_work',
        ),
        migrations.RemoveField(
            model_name='member',
            name='name',
        ),
        migrations.RemoveField(
            model_name='member',
            name='phone_num_long',
        ),
        migrations.RemoveField(
            model_name='member',
            name='phone_num_short',
        ),
        migrations.RemoveField(
            model_name='member',
            name='qq',
        ),
        migrations.RemoveField(
            model_name='member',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='member',
            name='wechat',
        ),
    ]
