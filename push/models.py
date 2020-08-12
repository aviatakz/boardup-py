from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.
from user.models import User


class MobileDevice(models.Model):
    participant = models.OneToOneField(User, related_name='device', on_delete=models.CASCADE)
    platform = models.CharField(max_length=20, choices=(('iOS', 'iOS'), ('Android', 'Android'),))
    registration_id = models.TextField()
    device_id = models.TextField()


class MobileNotification(models.Model):
    recipient = models.ForeignKey(User, related_name='user_device_notifications', on_delete=models.CASCADE)
    title = models.CharField(max_length=512, null=True, blank=True)
    message = models.TextField(default='')
    status = models.CharField(max_length=10, default='unread')
    data = JSONField()
    is_received = models.BooleanField(default=False)

