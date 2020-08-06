from django.urls import path, include
from rest_framework.routers import DefaultRouter

from push import views

router = DefaultRouter()
router.register(r'devices', views.DeviceViewSet, basename="Devices")
router.register(r'notifications', views.NotificationViewSet, basename="Notifications")

urlpatterns = [
    path('', include(router.urls))
]