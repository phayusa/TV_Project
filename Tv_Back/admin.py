# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.

admin.site.register(CategoryChannel)
admin.site.register(Tag)
admin.site.register(Channel)
admin.site.register(Movie)
admin.site.register(CategoryMovie)
admin.site.register(Client)
admin.site.register(CategorySerie)
admin.site.register(Serie)
admin.site.register(Season)
admin.site.register(Episode)

