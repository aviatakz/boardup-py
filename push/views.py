from rest_framework import viewsets

from .models import MobileDevice, MobileNotification
from .serializers import DeviceSerializer, NotificationSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = MobileDevice.objects.all()
    serializer_class = DeviceSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = MobileNotification.objects.all()
    serializer_class = NotificationSerializer
