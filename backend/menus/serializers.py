from rest_framework import serializers

from .models import Menu


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for menu model."""

    class Meta:
        model = Menu
        fields = "__all__"
