# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework.test import force_authenticate

from Tv_Back.models import Stream
from Tv_Back.serializers import StreamSerializer


class StreamBase(generics.GenericAPIView):
    serializer_class = StreamSerializer
    queryset = Stream.objects.all()
    # permission_classes = (ClientPermission, )

    def dispatch(self, request, *args, **kwargs):
        force_authenticate(request)
        return super(StreamBase, self).dispatch(request, *args, **kwargs)


class StreamList(StreamBase, generics.ListAPIView):
    # Filter by overriding because of encoding error
    def get_queryset(self):
        queryset = Stream.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        info = self.request.query_params.get('info', None)
        if info is not None:
            queryset = queryset.filter(extra_info=info)
        return queryset


class StreamCreate(StreamBase, generics.CreateAPIView):
    pass


class StreamDetail(StreamBase, generics.RetrieveUpdateDestroyAPIView):
    pass
