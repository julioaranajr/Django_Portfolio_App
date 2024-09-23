# projects/admin.py

from django.contrib import admin
from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'pub_date']
    search_fields = ['title', 'description', 'technology', 'status', 'pub_date']
    list_filter = ['technology', 'status', 'pub_date']
    list_per_page = 10


admin.site.register(Project, ProjectAdmin)
