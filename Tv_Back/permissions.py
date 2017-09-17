from rest_framework import permissions
from models import Client
from datetime import datetime


class ClientPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # device_id = request.resolver_match.kwargs.get('device_id')
        # device_id = request.data.get('device_id', False)
        if request.user.is_superuser:
            return True
        if not ('Authorisation' in request.META.keys()):
            return False
        device_id = request.META['Authorisation']
        # token = request.data.get('token', False)
        # if not device_id or not token:
        if not device_id:
            return False
        user = Client.objects.filter(device_id=device_id)[0]
        if not user:
            return False
        # white_addr = user.ip_connected.split(',')
        # return user.expiration_date > datetime.now() and request.META['REMOTE_ADDR'] in white_addr
        return user.expiration_date > datetime.now()

