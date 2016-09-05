from django.shortcuts import render

from rest_framework import permissions
from rest_framework import generics
from .permissions import IsOwner

from .serializers import CartSerializer
from .models import Cart


# Create your views here.
class CartList(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_classes = (IsOwner,)
