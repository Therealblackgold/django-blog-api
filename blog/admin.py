from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogModel(admin.ModelAdmin):
    list_filter = ("title", "date")
    list_display = ("title", "date")
