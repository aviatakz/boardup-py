from django.contrib.auth.models import User, Group
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer


class UsersByGroupSet(viewsets.ViewSet):
    def list(self, request, pk=None):
        group = Group.objects.get(id=pk)
        queryset = group.user_set.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
