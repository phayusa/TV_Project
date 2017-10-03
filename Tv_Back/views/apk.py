# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from wsgiref.util import FileWrapper

from django.http import HttpResponse

from TV_Project.settings import VERSION_APP

import os


def get_version(request):
    return HttpResponse(VERSION_APP)


def get_last_version(request):
    filename = "/Users/msrouji/MyDocuments/app-debug.apk"
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(filename)
    response['Content-Length'] = os.path.getsize(filename)
    return response
