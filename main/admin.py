from django.contrib import admin
from .models import (
    CustomUser, Achievements, About, Contact,
    Gallery, Question, IPLog
)

# ============================
# Custom User
# ============================
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff", "is_active")
    search_fields = ("username", "email")
    list_filter = ("is_staff", "is_active", "date_joined")
    ordering = ("username",)


# ============================
# Achievements
# ============================
@admin.register(Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "created_at", "is_active")
    list_filter = ("is_active", "created_at")
    search_fields = ("title", "description")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)


# ============================
# About
# ============================
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "created_at", "updated_at", "is_active")
    list_filter = ("is_active", "created_at")
    search_fields = ("title", "description")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)


# ============================
# Contact
# ============================
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("title", "social_account_name", "social_account_link", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "social_account_name")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("title",)


# ============================
# Gallery
# ============================
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "created_at", "is_active")
    list_filter = ("is_active", "created_at")
    search_fields = ("title",)
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)


# ============================
# Question
# ============================
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("name", "question", "is_active", "answered_by", "answered_at")
    list_filter = ("is_active",)
    search_fields = ("name", "question")
    readonly_fields = ("created_at", "answered_at")
    ordering = ("-created_at",)


# ============================
# IPLog
# ============================
@admin.register(IPLog)
class IPLogAdmin(admin.ModelAdmin):
    list_display = ("ip", "path", "count")
    search_fields = ("ip", "path")
    ordering = ("-count",)
