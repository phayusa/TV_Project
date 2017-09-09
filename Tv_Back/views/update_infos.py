# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import urllib2

from Tv_Back.models.serie import Serie
from Tv_Back.models.stream import Movie
from Tv_Back.models.category import CategorySerie, CategoryMovie
from django import http


def update_info(request):
    update_serie()
    #update_movie()

    return http.HttpResponseRedirect('/admin/')


def update_serie():
    base_url_api = "http://api.tvmaze.com/search/shows?q="
    for serie in Serie.objects.all():
        name_serie = serie.name.encode('utf-8')
        url = base_url_api.encode('utf-8') + name_serie

        json_received = urllib2.urlopen(url).read()
        object_movie = json.loads(json_received)[0]['show']
        serie.image_url = object_movie['image']['medium']
        serie.summary = object_movie['summary']
        for category in object_movie['genres']:
            find_category, _ = CategorySerie.objects.get_or_create(name=category)
            serie.category.add(find_category)
        serie.save()


def update_movie():
    base_url_api = "http://www.omdbapi.com/?t="
    for movie in Movie.objects.all():
        name_serie = movie.name.encode('utf-8')
        url = base_url_api.encode('utf-8') + name_serie

        json_received = urllib2.urlopen(url).read()
        object_movie = json.loads(json_received)[0]
        movie.image_url = object_movie['Poster']
        movie.summary = object_movie['Plot']
        for category in object_movie['Genre'].split(','):
            find_category, _ = CategoryMovie.objects.get_or_create(name=category)
            movie.category.add(find_category)
        movie.save()

