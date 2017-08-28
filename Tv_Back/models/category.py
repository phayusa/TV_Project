# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(blank=False, max_length=3)

    def __str__(self):
        return self.name
