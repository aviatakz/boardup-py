from django.conf import settings
from pyfcm import FCMNotification
from .models import MobileNotification
from user.models import User


def send_notification(obj):
    recipient = User.objects.get(id=obj.get("recipient_id"))
    notification = MobileNotification()
    notification.recipient = recipient
    interview_count = recipient.interviews.all().count()
    notification.title = f"You have {interview_count} interviews"

    data_payload = {
        "alert": notification.title,
        "notification_id": notification.pk
    }
    fcm = FCMNotification(api_key=settings.FIREBASE_API_KEY)

    return fcm.notify_single_device(
        registration_id=str(recipient.device.registration_id),
        data_message=data_payload)
