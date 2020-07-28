from push.models import MobileDevice, MobileNotification
from survey import serializers


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileDevice
        fields = ('id', 'participant', 'platform', 'registration_id', 'device_id')


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = MobileNotification
        fields = ('id', 'recepient', 'title', 'message', 'status', 'data')