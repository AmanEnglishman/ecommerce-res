from django.contrib import admin

from apps.menu.models import Menu, Category, Weight


class WeightInline(admin.TabularInline):
    model = Weight


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [WeightInline]


@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    None
