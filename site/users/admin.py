from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    readonly_fields = ('date_joined', 'last_login')
    list_display = (
        'username', 'email', 'is_staff', 'is_superuser'
        )
    ordering = ('username',)
    search_fields = ('username', 'email')
    list_display_links = ('username',)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (
            'Информация', {'fields': ('birthday_date', 'avatar')}
        ),
        (
            'Права и разрешения', {
                'fields': (
                    'is_active', 'is_staff', 'is_superuser', 'groups',
                    'user_permissions'
                    )
            }
        ),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
