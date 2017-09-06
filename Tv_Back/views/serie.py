# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework.test import force_authenticate

from Tv_Back.models import Season, Episode
from Tv_Back.serializers import SeasonSerializer, EpisodeSerializer


class SerieBase(generics.GenericAPIView):
    serializer_class = SeasonSerializer
    queryset = Season.objects.all()

    # permission_classes = (ClientPermission, )

    def dispatch(self, request, *args, **kwargs):
        force_authenticate(request)
        return super(SerieBase, self).dispatch(request, *args, **kwargs)


class SeasonList(SerieBase, generics.ListAPIView):
    # Filter by overriding because of encoding error
    def get_queryset(self):
        queryset = Season.objects.all()
        serie = self.request.query_params.get('serie', None)
        if serie is not None:
            queryset = queryset.filter(serie=serie)
        return queryset


class EpisodeList(SerieBase, generics.ListAPIView):
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all()

    # Filter by overriding because of encoding error
    def get_queryset(self):
        queryset = Episode.objects.all()
        season = self.request.query_params.get('season', None)
        if season is not None:
            queryset = queryset.filter(season=season)
        return queryset
