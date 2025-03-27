from django.contrib import admin
from . import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = 'first_name', 'last_name',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 20
    list_editable = 'phone',
    list_display_links = 'id', 'first_name', 'last_name',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',