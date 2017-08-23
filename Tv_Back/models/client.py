# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    authorized_to_access = models.BooleanField(default=False)
    ip_connected = models.CharField(max_length=20, blank=True)
    expiration_date = models.DateTimeField(blank=True, default=None)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.user.username
