from django.shortcuts import render

# Create your views here.
from .serializers import DeviceSerializer, NotificationSerializer
from rest_framework import viewsets

from push.models import MobileDevice, MobileNotification


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = MobileDevice.objects.all()
    serializer_class = DeviceSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = MobileNotification.objects.all()
    serializer_class = NotificationSerializer