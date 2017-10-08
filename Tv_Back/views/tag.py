# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework.test import force_authenticate

from Tv_Back.models import Tag
from Tv_Back.permissions import ClientPermissionStream
from Tv_Back.serializers import TagSerializer


class TagBase(generics.GenericAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = (ClientPermissionStream,)

    def dispatch(self, request, *args, **kwargs):
        force_authenticate(request)
        return super(TagBase, self).dispatch(request, *args, **kwargs)


class TagList(TagBase, generics.ListAPIView):
    pass
