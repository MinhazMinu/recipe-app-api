"""Django admin customizations for the core app."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


class UserAdmin(BaseUserAdmin):
    """Customize the admin interface for the User model."""

    ordering = ["id"]
    list_display = ["email", "name"]


admin.site.register(models.User, UserAdmin)
