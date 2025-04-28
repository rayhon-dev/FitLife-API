from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfile


class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('id', 'username', 'email', 'date_of_birth', 'gender', 'is_staff', 'is_active')
    list_filter = ('gender', 'is_staff', 'is_active', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('id',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('date_of_birth', 'gender')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_of_birth', 'gender', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'height', 'weight', 'activity_level', 'goal')
    search_fields = ('user__username', 'user__email')
    list_filter = ('activity_level', 'goal')
    ordering = ('id',)


admin.site.register(User, UserAdmin)
