import uuid

from django.db import models
from menu_items.models import MenuItem


class Menu(models.Model):
    """Menu card database model."""

    app_label = "menus"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(unique=True, max_length=50)
    description = models.TextField(null=False, max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    items = models.ManyToManyField(MenuItem, blank=True, related_name="menus")

    def __str__(self):
        return f"Menu {self.name} created at {self.created_at} last update {self.updated_at}"
