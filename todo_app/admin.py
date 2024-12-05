from django.contrib import admin
from .models import Task, Tag

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date', 'timestamp')
    list_filter = ('status', 'due_date', 'tags')  # Add filters
    search_fields = ('title', 'description')  # Add search functionality
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'due_date', 'status', 'tags')
        }),
        ('Timestamp', {
            'fields': ('timestamp',),
            'classes': ('collapse',),
        }),
    )

admin.site.register(Task, TaskAdmin)
admin.site.register(Tag)
