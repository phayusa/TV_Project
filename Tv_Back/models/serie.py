# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from category import CategorySerie


class Serie(models.Model):
    name = models.CharField(max_length=100)
    seasons = models.IntegerField(blank=True, null=True)
    episodes = models.IntegerField(blank=True, null=True)
    category = models.ManyToManyField(CategorySerie)
    image_url = models.URLField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.name
        # def __str__(self):
        # return self.name
