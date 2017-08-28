# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os,io

from rest_framework import status
from rest_framework.response import Response

from Tv_Back.models.category import Category
from Tv_Back.models.stream import Stream


def populate_db(request):
    home = os.getenv("HOME", "/home/phayusa")
    folder = home + "/TV_URL/"
    for dir_name in os.listdir(folder):
        for file_name in os.listdir(folder+dir_name):
            for line in io.open(folder+dir_name+"/"+file_name, encoding="utf-8").readlines():
                if line.startswith("#"):
                    name_channel = line.split(":")[2]
                    category, created = Category.objects.get_or_create(name=os.path.basename(file_name), type=os.path.basename(dir_name))
                else:
                    _, _ = Stream.objects.get_or_create(name=name_channel, url=line, category=category)
    return Response("Update validated", status=status.HTTP_201_CREATED)
