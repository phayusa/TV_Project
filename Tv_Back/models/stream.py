# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from .category import Category


class Stream(models.Model):
    name = models.CharField(blank=False, max_length=200)
    url = models.CharField(blank=False, max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    extra_info = models.CharField(blank=True, max_length=10)

    def __str__(self):
        return self.name
