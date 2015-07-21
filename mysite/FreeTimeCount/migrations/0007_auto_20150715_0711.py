# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FreeTimeCount', '0006_auto_20150715_0654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursetable',
            name='member',
        ),
        migrations.AddField(
            model_name='coursetable',
            name='student',
            field=models.ForeignKey(default=0, to='FreeTimeCount.Students'),
            preserve_default=False,
        ),
    ]
