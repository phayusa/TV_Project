# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from category import CategoryChannel, CategoryMovie
from season import Season


class Stream(models.Model):
    name = models.CharField(blank=False, max_length=200)
    url = models.CharField(blank=False, max_length=1000)

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        abstract = True


class Channel(Stream):
    category = models.ForeignKey(CategoryChannel, on_delete=models.CASCADE)


class Movie(Stream):
    category = models.ForeignKey(CategoryMovie)
    image_url = models.URLField(blank=True, null=True)


class Episode(models.Model):
    url = models.CharField(blank=False, max_length=1000)
    title = models.CharField(blank=True, null=True, max_length=1000)

    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    number = models.IntegerField()

    # def __unicode__(self):
    #       return u'%s season %s episode %s ' % (self.season.serie.name, self.season.number, self.number)

    def __str__(self):
        return self.season.serie.name + " season " + str(self.season.number) + " episode " + str(self.number)
