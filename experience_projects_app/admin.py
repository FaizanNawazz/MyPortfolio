from django.contrib import admin
from .models import ProjectExperience

@admin.register(ProjectExperience)
class ProjectExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'item_type', 'duration')
    list_filter = ('item_type',)
