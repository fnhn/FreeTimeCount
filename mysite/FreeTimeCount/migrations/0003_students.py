# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FreeTimeCount', '0002_auto_20150714_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stu_no', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('college', models.CharField(max_length=20)),
                ('major', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=3)),
            ],
        ),
    ]
