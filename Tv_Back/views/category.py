# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from Tv_Back.serializers import CategorySerializer
from Tv_Back.models import Category
from Tv_Back.permissions import ClientPermission
from rest_framework.test import force_authenticate


class CategoryBase(generics.GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # permission_classes = (ClientPermission, )

    def dispatch(self, request, *args, **kwargs):
        force_authenticate(request)
        return super(CategoryBase, self).dispatch(request, *args, **kwargs)


class CategoryList(CategoryBase, generics.ListAPIView):
    def get_queryset(self):
        queryset = Category.objects.all()
        type = self.request.query_params.get('type', None)
        if type is not None:
            queryset = queryset.filter(type=type)
        return queryset


class CategoryDetail(CategoryBase, generics.RetrieveUpdateDestroyAPIView):
    pass
