from django.urls import path
from .views import UserList, UserDetail, GroupList, GroupDetail
urlpatterns = [
    path('users/',UserList.as_view()),
    path(r'users/<int:pk>', UserDetail.as_view()),
    path('groups/', GroupList.as_view()),
    path('groups/<int:pk>', GroupDetail.as_view())
    ]