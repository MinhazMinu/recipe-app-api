"""Django admin customizations for the core app."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Customize the admin interface for the User model."""

    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name",)}),
        (
            _("Permissions"),
            {"fields": ("is_active", "is_staff", "is_superuser")},
        ),  # noqa
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    #  add from admin page
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },  # noqa
        ),  # noqa
    )

    readonly_fields = ["last_login"]


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Recipe)
