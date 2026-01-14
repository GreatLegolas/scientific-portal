from django.db import models
from django.conf import settings
from articles.models import Article

class Review(models.Model):
    """
    Review model for anonymous peer reviews.
    Ensures anonymity between authors and reviewers.
    """
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    RECOMMENDATION_CHOICES = [
        ('accept', 'Accept'),
        ('minor_revision', 'Minor Revision'),
        ('major_revision', 'Major Revision'),
        ('reject', 'Reject'),
    ]

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews_given')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    recommendation = models.CharField(max_length=20, choices=RECOMMENDATION_CHOICES, null=True, blank=True)
    comments = models.TextField(blank=True, help_text="Review comments (anonymous to author)")
    confidential_comments = models.TextField(blank=True, help_text="Comments for editors only")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['article', 'reviewer']

    def __str__(self):
        return f"Review of '{self.article.title}' by {self.reviewer.username}"

