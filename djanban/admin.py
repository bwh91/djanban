from django.contrib import admin
from . models import Project, Story

class ProjectAdmin(admin.ModelAdmin):
    pass

class StoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Story, StoryAdmin)

