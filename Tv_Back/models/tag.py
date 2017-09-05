# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Tv_Back.models.type import Type


class Tag(models.Model):
    name = models.CharField(max_length=1000)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
