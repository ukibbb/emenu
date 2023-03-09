from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class MyUserAdmin(UserAdmin):
    list_display = (
        "email",
        "is_staff",
        "is_active",
        "is_superuser",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser")}),
    )
    ordering = ("email",)
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )
    # readonly_fields = ("date_joined",)


admin.site.register(User, MyUserAdmin)
