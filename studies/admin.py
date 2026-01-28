from django.contrib import admin
from .models import StudySession


@admin.register(StudySession)
class StudySessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'topic', 'planned_duration', 'actual_duration', 'status', 'score')
    list_filter = ('status', 'date', 'difficulty')
    search_fields = ('user__username', 'topic')
    ordering = ('-date', '-created_at')
    readonly_fields = ('started_at', 'created_at', 'updated_at')
