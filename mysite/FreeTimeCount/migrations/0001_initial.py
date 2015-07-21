# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weekday', models.IntegerField()),
                ('time', models.CharField(max_length=10)),
                ('course_name', models.CharField(max_length=32)),
                ('place', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='CourseTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stu_id', models.IntegerField()),
                ('course_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('stuID', models.CharField(max_length=20)),
                ('dormitory', models.CharField(max_length=20)),
                ('phone_num_long', models.CharField(max_length=20)),
                ('phone_num_short', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('is_work', models.IntegerField()),
                ('qq', models.CharField(max_length=20)),
                ('wechat', models.CharField(max_length=20)),
            ],
        ),
    ]
