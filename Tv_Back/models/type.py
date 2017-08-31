# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=7)

    def __str__(self):
        return self.name
