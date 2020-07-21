from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('google/', views.GoogleLogin.as_view(), name='google_login'),
    path('login/', obtain_jwt_token),
]