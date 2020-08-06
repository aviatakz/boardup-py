from django.contrib import admin

# Register your models here.
from .models import MobileDevice, MobileNotification


class MobileDeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'participant', 'platform', 'registration_id', 'device_id')


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipient', 'title', 'message', 'status', 'data')


admin.site.register(MobileDevice, MobileDeviceAdmin)
admin.site.register(MobileNotification, NotificationAdmin)