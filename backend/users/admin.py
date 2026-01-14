from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'email_verified', 'orcid_id', 'created_at']
    list_filter = ['email_verified', 'is_staff', 'is_active', 'created_at']
    search_fields = ['username', 'email', 'orcid_id']
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('email_verified', 'orcid_id', 'bio', 'affiliation')}),
    )
    
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('email', 'email_verified', 'orcid_id', 'bio', 'affiliation')}),
    )

