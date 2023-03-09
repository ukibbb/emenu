from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import MenuItem
from .serializers import MenuItemSerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    """View for managing MenuItem CRUD operations."""

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = (IsAuthenticated,)
