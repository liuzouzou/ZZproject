# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-10-02 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20191002_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='pwd',
            field=models.CharField(max_length=128, verbose_name='密码'),
        ),
    ]
