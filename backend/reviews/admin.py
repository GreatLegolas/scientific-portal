from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['article', 'reviewer', 'status', 'recommendation', 'created_at', 'completed_at']
    list_filter = ['status', 'recommendation', 'created_at', 'completed_at']
    search_fields = ['article__title', 'reviewer__username', 'comments']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Review Information', {
            'fields': ('article', 'reviewer', 'status', 'recommendation')
        }),
        ('Comments', {
            'fields': ('comments', 'confidential_comments')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'completed_at')
        }),
    )

