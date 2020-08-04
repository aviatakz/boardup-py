from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models
from pyfcm import FCMNotification

from rating_back import settings
from survey.models import Interview


class MobileDevice(models.Model):
    participant = models.OneToOneField(User, related_name='device', on_delete=models.CASCADE)
    platform = models.CharField(max_length=20, choices=(('iOS', 'iOS'), ('Android', 'Android'),))
    registration_id = models.TextField()
    device_id = models.TextField()


class MobileNotification(models.Model):
    recipient = models.ForeignKey(User, related_name='user_device_notifications', on_delete=models.CASCADE)
    title = models.CharField(max_length=512, null=True, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=10, default='unread')
    data = JSONField()

    def send_notification(**self):
        recipient = User.objects.get(id=self.get("recipient_id"))
        notification = MobileNotification()
        notification.recipient = recipient
        interview_count = recipient.interviews.all().count()
        notification.title = f"You have {interview_count} interviews"

        if recipient.has_android_device():
            data_payload = {
                "alert": notification.title,
                "notification_id": notification.pk
            }
            fcm = FCMNotification(api_key=settings.FIREBASE_API_KEY)

            return fcm.notify_single_device(
                registration_id=str(recipient.device.registration_id),
                data_message=data_payload)