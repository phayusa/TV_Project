# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    authorized_to_access = models.BooleanField(default=False)
    ip_connected = models.CharField(max_length=20, blank=True)
    expiration_date = models.DateTimeField(blank=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, blank=False)

    def __str__(self):
        return self.user.username
