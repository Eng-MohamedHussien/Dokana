from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.models import LogEntry

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('name', 'email', 'mobile_number', 'another_mobile', 'created', 'updated', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('created', 'updated', 'is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('name', 'email', 'mobile_number', 'password')}),
        ('Permissions', {'fields': ('is_active',)}),
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', )
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'mobile_number', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    search_fields = ('email',)
    ordering = ('created',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(LogEntry)