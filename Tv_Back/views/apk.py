# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from wsgiref.util import FileWrapper

from django.http import HttpResponse
from rest_framework import status

from TV_Project.settings import VERSION_APP


def get_version(request):
    return HttpResponse(VERSION_APP)


def get_last_version(request):
    # if not request.META:
    #     return HttpResponse(status=status.HTTP_403_FORBIDDEN)
    # if not ("X_Sender_X" in request.META):
    #     return HttpResponse(status=status.HTTP_403_FORBIDDEN)
    # key = request.META.get("X_Sender_X")
    # if not key:
    #     return HttpResponse(status=status.HTTP_403_FORBIDDEN)
    # if not key == "32estloinTROPloin31565A/*":
    #     return HttpResponse(status=status.HTTP_403_FORBIDDEN)
    # filename = "/Users/msrouji/MyDocuments/app-debug.apk"
    filename = "/home/TV_Project/app-debug.apk"
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(filename)
    response['Content-Length'] = os.path.getsize(filename)
    return response
