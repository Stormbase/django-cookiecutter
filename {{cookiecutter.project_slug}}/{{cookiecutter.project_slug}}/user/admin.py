from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AbstractUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(AbstractUserAdmin):
    list_display = ["__str__", "is_active", "is_staff", "is_superuser"]
    list_filter = ["is_active", "is_staff", "is_superuser", "groups"]
    ordering = ["email"]
    search_fields = ["email"]
    fieldsets = (
        (None, {"fields": ["username", "password",]}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email",)},),
        (
            _("Permissions"),
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ]
            },
        ),
        (_("Important dates"), {"fields": ["last_login", "date_joined"]}),
    )
    add_fieldsets = (
        (None, {"classes": ["wide"], "fields": ["email", "password1", "password2"]},),
    )
