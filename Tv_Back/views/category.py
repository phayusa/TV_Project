# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from Tv_Back.serializers import CategorySerializer, CategoryChannelSerializer
from Tv_Back.models import CategoryChannel, CategoryMovie, CategorySerie
from Tv_Back.permissions import ClientPermission
from rest_framework.test import force_authenticate


class CategoryBase(generics.GenericAPIView):
    serializer_class = CategorySerializer
    # permission_classes = (ClientPermission, )

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


class CategorySerieList(CategoryBase, generics.ListAPIView):
    queryset = CategorySerie.objects.all()

# class CategoryDetail(CategoryBase, generics.RetrieveUpdateDestroyAPIView):
    # pass
