# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tv_Back', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='expiration_date',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]
