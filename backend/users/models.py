from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    Includes email verification and ORCID placeholder.
    """
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    orcid_id = models.CharField(max_length=19, blank=True, null=True, help_text="ORCID account ID (placeholder)")
    bio = models.TextField(blank=True)
    affiliation = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.username

