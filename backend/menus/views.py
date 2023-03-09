from django.core.cache import cache
from django.db.models import Count
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters import rest_framework as rest_filters
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from .filters import MenusFilter
from .models import Menu
from .serializers import MenuSerializer


class MenuViewSet(viewsets.ModelViewSet):
    """View for managing Menu CRUD operations."""

    queryset = (
        Menu.objects.prefetch_related("items")
        .filter(items__isnull=False)
        .annotate(items_count=Count("items"))
    )
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        rest_filters.DjangoFilterBackend,
    ]
    filterset_class = MenusFilter

    search_fields = ["name"]
    ordering_fields = ["name", "items_count"]

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)

    @method_decorator(cache_page(60 * 60 * 2))
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)

    def create(self, *args, **kwargs):
        cache.clear()
        return super().create(*args, **kwargs)

    def update(self, *args, **kwargs):
        cache.clear()
        return super().update(*args, **kwargs)

    def partial_update(self, *args, **kwargs):
        cache.clear()
        return super().partial_update(*args, **kwargs)

    def destroy(self, *args, **kwargs):
        cache.clear()
        return super().destroy(*args, **kwargs)
