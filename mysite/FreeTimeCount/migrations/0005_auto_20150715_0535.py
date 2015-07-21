# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FreeTimeCount', '0004_auto_20150715_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=0, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='students',
            name='stu_no',
            field=models.CharField(max_length=10),
        ),
    ]
