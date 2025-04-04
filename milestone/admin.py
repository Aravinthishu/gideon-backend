from django.contrib import admin
from .models import Milestone, MilestoneImage

class MilestoneImageInline(admin.TabularInline):  # Use StackedInline for a vertical layout
    model = MilestoneImage
    extra = 1  # Number of empty image slots

@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')
    inlines = [MilestoneImageInline]
