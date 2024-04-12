from django.contrib import admin

from .models import MyUser, User


@admin.register(MyUser)
class CustomUserAdmin(admin.ModelAdmin):
    None

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    None

