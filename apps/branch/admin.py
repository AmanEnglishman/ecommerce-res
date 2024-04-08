from django.contrib import admin
from apps.branch.models import (Branch, BranchImages, BranchNumber,
                                Booth, BoothImages)


class BranchInline(admin.TabularInline):
    model = BranchNumber
    extra = 5


class BranchImagesInline(admin.TabularInline):
    model = BranchImages
    extra = 5


class BoothImagesInline(admin.TabularInline):
    model = BoothImages
    extra = 5


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    inlines = [BranchInline, BranchImagesInline]


@admin.register(Booth)
class BoothAdmin(admin.ModelAdmin):
    inlines = [BoothImagesInline]
