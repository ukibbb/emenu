from rest_framework import serializers

from .models import MenuItem


class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    """MenuItem models serializer."""

    class Meta:
        model = MenuItem
        fields = "__all__"
