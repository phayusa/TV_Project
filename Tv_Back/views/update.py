# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import io
import os

from django import http

from Tv_Back.models.category import CategoryChannel, CategorySerie, CategoryMovie
from Tv_Back.models.stream import Channel, Movie, Episode
from Tv_Back.models.tag import Tag
from Tv_Back.models.serie import Serie
from Tv_Back.models.season import Season


def populate_db(request):
    # if not request.user.isAdmin:
    #     return Response("Forbidden", status=status.HTTP_403_FORBIDDEN)

    home = os.getenv("HOME", "/home/phayusa")
    folder = home + "/TV_URL/"
    episodes = 1
    for dir_name in os.listdir(folder):
        for file_name in os.listdir(folder + dir_name):
            for line in io.open(folder + dir_name + "/" + file_name.replace("._",""), encoding="utf-8").readlines():
                if line.startswith("﻿#"):
                    name_channel_raw = line.split(",")[1].strip()
                    tag_name = "None"
                    if ":" in name_channel_raw:
                        infos = name_channel_raw.split(":")
                        name_channel_raw = infos[1]
                        tag_name = infos[0]
                    type_stream = dir_name.encode("utf-8")
                    name_channel = name_channel_raw
                    if type_stream == "channels":
                        tag, _ = Tag.objects.get_or_create(name=tag_name)

                        category, created = CategoryChannel.objects.get_or_create(
                            name=os.path.basename(file_name).rsplit('.', 1)[0].encode("utf-8"),
                            tag=tag)

                        type_data = "channels"
                    else:
                        name_folder = os.path.basename(file_name).rsplit('.', 1)[0]
                        if "VOD" in name_folder:
                            type_data = "movie"
                            category, _ = CategoryMovie.objects.get_or_create(
                                name=name_folder.split("VOD ")[1].encode("utf-8"))
                        else:

                            serie_info = name_folder.split("S0")
                            name_serie = serie_info[0].strip()
                            number_season = serie_info[1].strip()
                            type_data = "episode " + name_serie + " " + number_season

                            # Create the serie
                            serie, _ = Serie.objects.get_or_create(name=name_serie)
                            serie.seasons = int(number_season)
                            serie.episodes = episodes
                            serie.save()

                            season, season_created = Season.objects.get_or_create(number=number_season, serie=serie)
                            if season_created:
                                episodes = 1
                            else:
                                season.episodes = episodes
                                season.save()
                            # category, _ = CategoryMovie.objects.get_or_create(
                            # name=name_serie)
                else:
                    if type_data == "channels":
                        _, _ = Channel.objects.get_or_create(name=name_channel, url=line.strip().encode("utf-8"),
                                                             category=category)
                    elif type_data == "movie":
                        _, _ = Movie.objects.get_or_create(name=name_channel, url=line.strip().encode("utf-8"),
                                                           category=category)
                    else:
                        _, _ = Episode.objects.get_or_create(season=season, number=episodes,
                                                             url=line.strip().encode("utf-8"))
                        episodes += 1

    return http.HttpResponseRedirect('/TV/update/infos/')
