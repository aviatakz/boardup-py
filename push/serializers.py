from rest_framework import serializers

from .models import MobileDevice, MobileNotification


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = MobileDevice
        fields = ('id', 'participant', 'platform', 'registration_id', 'device_id')


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = MobileNotification
        fields = ('id', 'recipient', 'title', 'message', 'status', 'data')
