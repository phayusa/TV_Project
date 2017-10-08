# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

import stripe
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import AllowAny

from Tv_Back.models import Client
from Tv_Back.permissions import ClientPermissionAccess


@method_decorator(csrf_exempt, name="dispatch")
class SendToken(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (ClientPermissionAccess,)

    def post(self, request, format=None):
        print request.user

        client = Client.objects.get(user=request.user)
        if not client:
            return Response("OK", status=status.HTTP_403_FORBIDDEN)

        token = request.data.get('token', False)
        if not token:
            return Response(status=status.HTTP_403_FORBIDDEN)

        # print token
        stripe.api_key = "sk_test_YGOG39KYYyL8RqRo2izM3fn8"

        # Charge the user's card:
        charge = stripe.Charge.create(
            amount=4200,
            currency="eur",
            description="Subscription 1 year for "+client.user.username,
            source=token,
        )
        if not charge:
            return Response("Error payment", status=status.HTTP_406_NOT_ACCEPTABLE)

        client.expiration_date = timezone.now() + datetime.timedelta(days=365)
        # if client.expiration_date < timezone.now():
        # client.expiration_date = timezone.now() + datetime.timedelta(days=365)
        # else:
        # client.expiration_date = client.expiration_date + datetime.timedelta(days=365)
        client.save()
        return Response("OK", status=status.HTTP_202_ACCEPTED)
