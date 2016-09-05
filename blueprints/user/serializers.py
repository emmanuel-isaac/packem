from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.ReadOnlyField()
    cart_set = serializers.HyperlinkedRelatedField(many=True, view_name='cart-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'cart_set', 'username', 'first_name', 'last_name', 'password', 'email', 'is_staff',)
