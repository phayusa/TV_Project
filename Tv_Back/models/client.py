# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    authorized_to_access = models.BooleanField(default=False)
    ip_connected = models.CharField(max_length=20, blank=True)
    expiration_date = models.DateTimeField()
    # user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    device_id = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.device_id
        # def __str__(self):
        # return self.user.username
