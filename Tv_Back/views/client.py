# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import http
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from Tv_Back.models import Client


class ClientCreate(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        username = request.data.get('username', False)
        password = request.data.get('password', False)
        mail = request.data.get('mail', False)

        if not mail and not username and not password:
            return Response("Username or Password or Mail not renseigned", status=status.HTTP_400_BAD_REQUEST)
        link_user = User.objects.filter(username=username, password=password, email=mail, is_active=False)
        if not link_user:
            link_user = User.objects.create_user(username=username, password=password, email=mail, is_active=False)
            link_user.save()
        token = default_token_generator.make_token(link_user)
        uid = urlsafe_base64_encode(force_bytes(link_user.pk))

        new_client = Client.objects.create(expiration_date=timezone.now(), user=link_user)
        new_client.save()

        url = 'http://127.0.0.1:8000/TV/validate/' + uid + '/' + token
        #try:
        send_mail('Activate your account', 'Activate at : %s' % url, 'courstesttt@@gmail.com', [mail])
        #except:
         #   link_user.delete()
          #  return Response("Error during the sending of mail", status=status.HTTP_409_CONFLICT)
        return Response("Please valid your account", status=status.HTTP_201_CREATED)


def activate(request, uidb64, token):
    if uidb64 is not None and token is not None:
        uid = urlsafe_base64_decode(uidb64)
        try:
            user_model = get_user_model()
            user = user_model.objects.get(pk=uid)
            if default_token_generator.check_token(user, token) and user.is_active == 0:
                user.is_active = True
                user.save()
                return http.HttpResponseRedirect('/TV/channels/')
        except:
            pass
    return http.HttpResponseRedirect('/user/logout/')
