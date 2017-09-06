# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from Tv_Back.models.tag import Tag


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.name
    # def __str__(self):
        # return self.name

    class Meta:
        abstract = True


class CategorySerie(Category):
    pass


class CategoryMovie(Category):
    pass


class CategoryChannel(Category):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
