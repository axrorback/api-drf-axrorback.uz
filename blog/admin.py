from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "created_at", "is_active")
    list_filter = ("is_active", "created_at")
    search_fields = ("title", "content")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)

    # Slug avtomatik hosil bo'lishi uchun
    prepopulated_fields = {"slug": ("title",)}
