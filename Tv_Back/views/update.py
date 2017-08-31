# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import io
import os

from django import http

from Tv_Back.models.category import Category
from Tv_Back.models.stream import Stream
from Tv_Back.models.type import Type


def populate_db(request):
    # if not request.user.isAdmin:
    #     return Response("Forbidden", status=status.HTTP_403_FORBIDDEN)

    home = os.getenv("HOME", "/home/phayusa")
    folder = home + "/TV_URL/"
    for dir_name in os.listdir(folder):
        for file_name in os.listdir(folder + dir_name):
            for line in io.open(folder + dir_name + "/" + file_name, encoding="utf-8").readlines():
                if line.startswith("﻿#"):
                    name_channel = line.split(",")[1].strip()
                    if ":" in name_channel:
                        name_channel = name_channel.split(":")[1]
                    name_channel = name_channel.encode("utf-8")
                    type_stream, _ = Type.objects.get_or_create(name=dir_name.encode("utf-8"))
                    category, created = Category.objects.get_or_create(
                        name=os.path.basename(file_name).rsplit('.', 1)[0].encode("utf-8"),
                        type=type_stream)
                else:
                    _, _ = Stream.objects.get_or_create(name=name_channel, url=line.strip().encode("utf-8"), category=category)
    return http.HttpResponseRedirect('/TV/channels/')
