# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from views.stream import ChannelList, MovieList, SerieList
from views.client import ClientCreate, activate
from views.category import CategoryChannelList, CategoryMovieList, CategorySerieList
from views.serie import SeasonList
from views.tag import TagList
from views.update import populate_db
from views.serie import EpisodeList

urlpatterns = [
    url(r'^channels/$', ChannelList.as_view()),
    url(r'^movies/$', MovieList.as_view()),
    url(r'^series/$', SerieList.as_view()),
    # url(r'^channel/(?P<pk>[0-9]+)/$', StreamDetail.as_view()),
    # url(r'^categories/', CategoryList.as_view()),

    url(r'^channels/tags/$', TagList.as_view()),
    url(r'^channels/categories/$', CategoryChannelList.as_view()),
    url(r'^movies/categories/$', CategoryMovieList.as_view()),
    url(r'^series/categories/$', CategorySerieList.as_view()),

    url(r'^series/seasons/$', SeasonList.as_view()),
    url(r'^series/episodes/$', EpisodeList.as_view()),

    url(r'create/', ClientCreate.as_view()),

    url(r'update/all/', populate_db, name="update"),
    url(r'validate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate,
        name='user-activation-link'),
]
