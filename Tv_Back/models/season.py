# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from serie import Serie


class Season(models.Model):
    number = models.IntegerField()
    episodes = models.IntegerField(blank=True, null=True)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s season %s' % (self.serie.name, self.number)
