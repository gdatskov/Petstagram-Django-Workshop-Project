from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from petstagram.accounts.forms import RegisterForm, EditForm

UserModel = get_user_model()


@admin.register(UserModel)
class Admin(UserAdmin):
    form = EditForm
    add_form = RegisterForm
    list_display = ("username", "email", "first_name", "last_name", "gender", "is_staff")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "gender")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
