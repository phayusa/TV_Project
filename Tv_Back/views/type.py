# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework.test import force_authenticate

from Tv_Back.models import Type
from Tv_Back.serializers import TypeSerializer


class TypeBase(generics.GenericAPIView):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
    # permission_classes = (ClientPermission, )

    def dispatch(self, request, *args, **kwargs):
        force_authenticate(request)
        return super(TypeBase, self).dispatch(request, *args, **kwargs)


class TypeList(TypeBase, generics.ListAPIView):
    pass
