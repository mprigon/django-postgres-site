from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import User
from personal.forms import ProfileUpdateForm
from core.forms import SignUpForm


class UserAdmin(BaseUserAdmin):
    form = ProfileUpdateForm
    add_form = SignUpForm
    list_display = ['username', 'email', 'skills', 'mobile_phone']
    list_filter = ['email']
    fieldsets = [
        (None, {'fields': ['username', 'password']}),
        ('Personal info', {'fields': ['email', 'skills', 'mobile_phone']}),
        ('Permissions', {'fields': []})

         ]
    add_fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['email', 'skills', 'mobile_phone',
                           'password1', 'password2'],
            },
        ),
    ]
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = []


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
