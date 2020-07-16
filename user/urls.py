from django.urls import path
from .views import UserList, UserDetail, GroupList, GroupDetail, UsersByGroupSet
urlpatterns = [
    path('users',UserList.as_view()),
    path(r'users/<int:pk>', UserDetail.as_view()),
    path('groups', GroupList.as_view()),
    path('groups/<int:pk>', GroupDetail.as_view()),
    path('users/group/<int:pk>', UsersByGroupSet.as_view({'get': 'list'}))
    ]