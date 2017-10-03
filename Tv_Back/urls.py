# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from views.stream import ChannelList, MovieList, SerieList
from views.client import ClientCreate, activate, LoginView
from views.category import CategoryChannelList, CategoryMovieList, CategorySerieList
from views.serie import SeasonList
from views.tag import TagList
from views.update import populate_db
from views.update_infos import update_info
from views.serie import EpisodeList
from views.client import subscription_extension
from views.payement import SendToken
from views.apk import get_version, get_last_version

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

    url(r'create/$', ClientCreate.as_view()),
    url(r'login/$', LoginView.as_view()),

    url(r'user/subscription', SendToken.as_view(), name="Reabo"),

    url(r'apk/version', get_version, name="version"),
    url(r'apk/file/last', get_last_version, name="apk"),

    url(r'update/all/', populate_db, name="update"),
    url(r'update/infos/', update_info, name="infos"),
    url(r'update/user/(?P<device_id>[0-9A-Za-z_.\-]+)', subscription_extension, name="extension"),
    url(r'user/time/(?P<device_id>[0-9A-Za-z_.\-]+)', subscription_extension, name="extension"),
    url(r'validate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate,
        name='user-activation-link'),
]
