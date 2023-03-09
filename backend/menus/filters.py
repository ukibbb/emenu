import django_filters as filters

from .models import Menu


class MenusFilter(filters.FilterSet):
    """Filtering menus."""

    created_at = filters.DateFromToRangeFilter()
    updated_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Menu
        fields = ("created_at", "updated_at")
