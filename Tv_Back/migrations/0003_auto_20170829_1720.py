# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-29 17:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tv_Back', '0002_auto_20170829_1718'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Format',
            new_name='Type',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='format',
            new_name='type',
        ),
    ]
