from django.contrib.auth.models import Group
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    @action(detail=False, methods=['patch'])
    def add_users(self, request):
        users_id = request.data["users"]
        groups_id = request.data["groups"]
        users = User.objects.filter(pk__in=users_id)
        groups = Group.objects.filter(pk__in=groups_id)
        for user in users:
            for group in groups:
                user.groups.add(group)
        return Response(status.HTTP_200_OK)

    @action(detail=False, methods=['patch'])
    def delete_users(self, request):
        users_id = request.data["users"]
        groups_id = request.data["groups"]
        users = User.objects.filter(pk__in=users_id)
        groups = Group.objects.filter(pk__in=groups_id)
        for user in users:
            for group in groups:
                user.groups.remove(group)
        return Response(status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ('groups',)
