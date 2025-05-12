from django.contrib import admin
from .models import Brand, Social_links, PrivacyPolicy

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ('name', 'googlemap_url', 'phone', 'email')
    list_filter = ('name',)
    ordering = ('name',)
    fields = ('name', 'googlemap_url', 'logo', 'fevicon', 'phone', 'email', 'email2', 'address')

@admin.register(Social_links)
class SocialLinksAdmin(admin.ModelAdmin):
    search_fields = ('name', 'url')
    list_filter = ('name',)
    ordering = ('name',)
    fields = ('name', 'url', 'icon')
    
admin.site.register(PrivacyPolicy)