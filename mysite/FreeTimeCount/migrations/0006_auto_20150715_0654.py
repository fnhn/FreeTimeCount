# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FreeTimeCount', '0005_auto_20150715_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='weekday',
            field=models.CharField(max_length=5),
        ),
    ]
