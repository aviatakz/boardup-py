from django.contrib.auth.models import User
from django.db import models
from rest_framework.fields import JSONField


class MobileDevice(models.Model):
    owner = models.OneToOneField(User, related_name='device', on_delete=models.CASCADE)
    platform = models.CharField(max_length=20, choices=(('iOS', 'iOS'), ('Android', 'Android'),))
    token = models.TextField()


class MobileNotification(models.Model):
    recipient = models.ForeignKey(User, related_name='user_device_notifications', on_delete=models.CASCADE)
    title = models.CharField(max_length=512, null=True, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=10, default='unread')
    data = JSONField()
