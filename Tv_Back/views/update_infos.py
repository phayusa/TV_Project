# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import urllib2
import re

from Tv_Back.models.serie import Serie
from Tv_Back.models.stream import Movie
from Tv_Back.models.category import CategorySerie, CategoryMovie
from django import http


def update_info(request):
    update_serie()
    # update_movie()

    return http.HttpResponseRedirect('/admin/')


def clean_html(raw_html):
    clean_r = re.compile('<.*?>')
    clean_text = re.sub(clean_r, '', raw_html)
    return clean_text


def update_serie():
    base_url_api = "http://api.tvmaze.com/search/shows?q="
    for serie in Serie.objects.all():
        name_serie = serie.name.encode('utf-8')
        url = base_url_api.encode('utf-8') + name_serie

        json_received = urllib2.urlopen(url).read()
        object_movie = json.loads(json_received)[0]['show']
        serie.image_url = object_movie['image']['medium']
        serie.summary = clean_html(object_movie['summary'])
        for category in object_movie['genres']:
            find_category, _ = CategorySerie.objects.get_or_create(name=category)
            serie.category.add(find_category)
        serie.save()


def update_movie():
    # base_url_api = "https://tv-v2.api-fetch.website/movies/1?keywords="
    base_url_api = "http://www.omdbapi.com/?apikey=BanMePls&t="
    headers = {
        'User-Agent': 'Mozilla/5.0'}
    for movie in Movie.objects.all():
        name_serie = movie.name.encode('utf-8').strip()
        print name_serie
        url = base_url_api.encode('utf-8') + name_serie
        print url
        req = urllib2.Request(url, None, headers)
        open_url = urllib2.urlopen(req)
        json_received = open_url.read()
        object_movie = json.loads(json_received)[0]
        movie.image_url = object_movie['Poster']
        movie.summary = object_movie['Plot']
        # for category in object_movie['genres']:
        #     find_category, _ = CategoryMovie.objects.get_or_create(name=category)
        #     movie.category.add(find_category)
        movie.save()
