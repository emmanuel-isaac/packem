from django.shortcuts import render

from rest_framework import permissions
from rest_framework import generics

from .models import User
from .serializers import UserSerializer
from .permissions import IsOwnerOrAdminOrReadOnly


class UserList(generics.ListCreateAPIView):
    """
    List all users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrAdminOrReadOnly,)
