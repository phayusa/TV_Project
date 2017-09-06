# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=1000)

    def __unicode__(self):
        return u'%s' % self.name

# def __str__(self):
#        return self.name
