from django.db import models
from django.conf import settings

class Article(models.Model):
    """
    Article model for storing scientific articles.
    Includes title, abstract, keywords and metadata.
    """
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=500)
    abstract = models.TextField()
    keywords = models.TextField(help_text="Comma-separated keywords")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    submitted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_keywords_list(self):
        """Return keywords as a list"""
        return [k.strip() for k in self.keywords.split(',') if k.strip()]

