# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import stripe
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from Tv_Back.models import Client


@method_decorator(csrf_exempt, name="dispatch")
class SendToken(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (ClientPermission,)
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        print request.user

        client = Client.objects.get(user=request.user)
        if not client:
            return Response("OK", status=status.HTTP_403_FORBIDDEN)

        token = request.data.get('token', False)
        if not token:
            return Response(status=status.HTTP_403_FORBIDDEN)

        print token
        stripe.api_key = "sk_test_YGOG39KYYyL8RqRo2izM3fn8"

        # Charge the user's card:
        charge = stripe.Charge.create(
            amount=1000,
            currency="eur",
            description="Example charge",
            source=token,
        )

        return Response("OK", status=status.HTTP_202_ACCEPTED)
