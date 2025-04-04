from django.contrib import admin
from .models import *

class MainProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')  # Display these fields in the admin list
    prepopulated_fields = {'slug': ('name',)}  # Auto-generate slug from name
    search_fields = ('name', 'description')  # Enable search by name and description
    list_filter = ('name',)  # Add filter by name

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'MainProduct', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description', 'MainProduct__name')  # Search across related MainProduct
    list_filter = ('MainProduct',)

admin.site.register(MainProduct, MainProductAdmin)
admin.site.register(Products, ProductsAdmin)
