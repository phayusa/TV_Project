# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework.test import force_authenticate
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from Tv_Back.models import CategoryChannel, CategoryMovie, CategorySerie
from Tv_Back.permissions import ClientPermission
from Tv_Back.serializers import CategorySerializer, CategoryChannelSerializer, CategoryMovieSerializer, \
    CategorySerieeSerializer


class CategoryBase(generics.GenericAPIView):
    serializer_class = CategorySerializer
    permission_classes = (ClientPermission,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def dispatch(self, request, *args, **kwargs):
        force_authenticate(request)
        return super(CategoryBase, self).dispatch(request, *args, **kwargs)


class CategoryChannelList(CategoryBase, generics.ListAPIView):
    queryset = CategoryChannel.objects.all()
    serializer_class = CategoryChannelSerializer

    def get_queryset(self):
        queryset = CategoryChannel.objects.all()
        tag = self.request.query_params.get('tag', None)
        if tag is not None:
            queryset = queryset.filter(tag=tag)
        return queryset


class CategoryMovieList(CategoryBase, generics.ListAPIView):
    queryset = CategoryMovie.objects.all()
    serializer_class = CategoryMovieSerializer


class CategorySerieList(CategoryBase, generics.ListAPIView):
    queryset = CategorySerie.objects.all()
    serializer_class = CategorySerieeSerializer

# class CategoryDetail(CategoryBase, generics.RetrieveUpdateDestroyAPIView):
# pass
