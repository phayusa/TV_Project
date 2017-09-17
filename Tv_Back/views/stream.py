# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework.test import force_authenticate

from Tv_Back.models import Channel, Movie, Serie
from Tv_Back.permissions import ClientPermission
from Tv_Back.serializers import ChannelSerializer, MovieSerializer, SerieSerializer


class StreamBase(generics.GenericAPIView):
    permission_classes = (ClientPermission, )

    def dispatch(self, request, *args, **kwargs):
        force_authenticate(request)
        return super(StreamBase, self).dispatch(request, *args, **kwargs)


class ChannelList(StreamBase, generics.ListAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    # Filter by overriding because of encoding error
    def get_queryset(self):
        queryset = Channel.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset


class MovieList(StreamBase, generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # Filter by overriding because of encoding error
    def get_queryset(self):
        queryset = Movie.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset


class SerieList(StreamBase, generics.ListAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

    # Filter by overriding because of encoding error
    def get_queryset(self):
        queryset = Serie.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset


