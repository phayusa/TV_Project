from django.utils import timezone
from rest_framework import permissions

from models import Client


class ClientPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # device_id = request.resolver_match.kwargs.get('device_id')
        # device_id = request.data.get('device_id', False)
        if request.user.is_superuser:
            return True
        # if not ('Authorisation' in request.META.keys()):
        # return False
        # device_id = request.META['Authorisation']
        # token = request.data.get('token', False)
        # if not device_id or not token:
        # if not device_id:
        #    return False
        client = Client.objects.filter(user=request.user)[0]
        if not client:
            return False
        else:
            return client.expiration_date > timezone.now()
            #return False
        # white_addr = user.ip_connected.split(',')
        # return user.expiration_date > datetime.now() and request.META['REMOTE_ADDR'] in white_addr
        # return user.expiration_date > datetime.now()
