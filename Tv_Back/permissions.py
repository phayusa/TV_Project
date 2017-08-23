from rest_framework import permissions
from models import Client


class ClientPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.is_superuser:
            return True
        user = Client.objects.filter(user=request.user)[0]
        if not user.ip_connected or not user:
            return False
        white_addr = user.ip_connected.split(',')
        return user.authorized_to_access and request.META['REMOTE_ADDR'] in white_addr

