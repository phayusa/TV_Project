# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import hashlib
import json

from django import http
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.http import urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from Tv_Back.models import Client


@method_decorator(csrf_exempt, name="dispatch")
class ClientCreate(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        # username = request.data.get('username', False)
        # password = request.data.get('password', False)
        # mail = request.data.get('mail', False)
        #
        # if not mail and not username and not password:
        #     return Response("Username or Password or Mail not renseigned", status=status.HTTP_400_BAD_REQUEST)
        # link_user = User.objects.filter(username=username, password=password, email=mail, is_active=False)
        # if not link_user:
        #     link_user = User.objects.create_user(username=username, password=password, email=mail, is_active=False)
        #     link_user.save()
        # token = default_token_generator.make_token(link_user)
        # uid = urlsafe_base64_encode(force_bytes(link_user.pk))

        id = request.data.get('id', False)
        print id
        if not id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        hash_obj = hashlib.sha256(id)
        password = hash_obj.hexdigest()

        if not User.objects.filter(username=id).exists():
            link_user = User.objects.create_user(username=id, password=password)
            link_user.save()
        else:
            link_user = User.objects.filter(username=id)

        # if Client.objects.get(device_id=id):
        #     return Response(status=status.HTTP_403_FORBIDDEN)
        new_client = Client.objects.create(expiration_date=timezone.now() + datetime.timedelta(days=+365),
                                           user=link_user)
        new_client.save()

        # url = 'http://127.0.0.1:8000/TV/validate/' + uid + '/' + token
        # # try:
        # send_mail('Activate your account', 'Activate at : %s' % url, 'courstesttt@@gmail.com', [mail])
        # except:
        #   link_user.delete()
        #  return Response("Error during the sending of mail", status=status.HTTP_409_CONFLICT)
        # return Response("Please valid your account", status=status.HTTP_201_CREATED)
        return Response("OK", status=status.HTTP_201_CREATED)


@method_decorator(csrf_exempt, name="dispatch")
class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, **kwargs):
        id = request.data.get('id', False)
        if not id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        username = id
        password = hashlib.sha256(id).hexdigest()
        print username

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)

            response = {'user': username}
            response.update({'token': token})
            return Response(response, status=status.HTTP_202_ACCEPTED)

            # return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        return Response(status=status.HTTP_400_BAD_REQUEST)


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


def subscription_extension(request, device_id):
    client = Client.objects.get(device_id=device_id)
    if not client:
        return Response("OK", status=status.HTTP_403_FORBIDDEN)
    # Add check of payement
    client.expiration_date = timezone.now() + datetime.timedelta(days=365)
    client.save()
    return Response("OK", status=status.HTTP_202_ACCEPTED)


def get_subscription(request, device_id):
    client = Client.objects.get(device_id=device_id)
    if not client:
        return Response("OK", status=status.HTTP_403_FORBIDDEN)
    # Add check of payement
    return Response(json.dump({'time': client.expiration_date}), status=status.HTTP_202_ACCEPTED)
