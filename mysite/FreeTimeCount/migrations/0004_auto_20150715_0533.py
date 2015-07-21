# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FreeTimeCount', '0003_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='id',
        ),
        migrations.AlterField(
            model_name='students',
            name='stu_no',
            field=models.CharField(max_length=10, serialize=False, primary_key=True),
        ),
    ]
