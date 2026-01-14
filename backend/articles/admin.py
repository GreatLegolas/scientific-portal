from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'view_count', 'created_at', 'submitted_at']
    list_filter = ['status', 'created_at', 'submitted_at']
    search_fields = ['title', 'abstract', 'keywords', 'author__username']
    readonly_fields = ['view_count', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Article Information', {
            'fields': ('title', 'abstract', 'keywords', 'author')
        }),
        ('Status', {
            'fields': ('status', 'submitted_at')
        }),
        ('Analytics', {
            'fields': ('view_count', 'created_at', 'updated_at')
        }),
    )

