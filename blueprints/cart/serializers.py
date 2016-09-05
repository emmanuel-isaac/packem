from rest_framework import serializers
from rest_framework import permissions

from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'items', 'hampers', 'paid_for', 'user', 'created',)
