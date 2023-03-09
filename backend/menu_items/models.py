import uuid

from django.db import models


class MenuItem(models.Model):
    """Menu item database model."""

    app_label = "menu_items"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=False, max_length=255)
    price = models.DecimalField(null=False, max_digits=6, decimal_places=2)
    preparation_time = models.TimeField(
        null=False, help_text="In minutes HH:mm:ss format"
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_vegetarian = models.BooleanField(default=False)

    def __str__(self):
        return f"Menu {self.name} created at {self.created_at} last update {self.updated_at}"
