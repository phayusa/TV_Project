# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from Tv_Back.serializers import StreamSerializer
from Tv_Back.models import Stream
from Tv_Back.permissions import ClientPermission
from rest_framework.test import force_authenticate


class StreamBase(generics.GenericAPIView):
    serializer_class = StreamSerializer
    queryset = Stream.objects.all()
    permission_classes = (ClientPermission, )

    def dispatch(self, request, *args, **kwargs):
        force_authenticate(request)
        return super(StreamBase, self).dispatch(request, *args, **kwargs)


class StreamList(StreamBase, generics.ListAPIView):
    pass


class StreamCreate(StreamBase, generics.CreateAPIView):
    pass


class StreamDetail(StreamBase, generics.RetrieveUpdateDestroyAPIView):
    pass
