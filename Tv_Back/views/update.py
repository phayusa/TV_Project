# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import io
import os

from django import http

from Tv_Back.models.category import Category
from Tv_Back.models.stream import Stream
from Tv_Back.models.type import Type
from Tv_Back.models.tag import Tag


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
                    tag_name = "None"
                    if ":" in name_channel:
                        infos = name_channel.split(":")
                        name_channel = infos[1]
                        tag_name = infos[0]
                    type_stream, _ = Type.objects.get_or_create(name=dir_name.encode("utf-8"))
                    tag, _ = Tag.objects.get_or_create(name=tag_name, type=type_stream)
                    name_channel = name_channel.encode("utf-8")
                    category, created = Category.objects.get_or_create(
                        name=os.path.basename(file_name).rsplit('.', 1)[0].encode("utf-8"),
                        tag=tag)
                else:
                    _, _ = Stream.objects.get_or_create(name=name_channel, url=line.strip().encode("utf-8"),
                                                        category=category)
    return http.HttpResponseRedirect('/TV/channels/')
