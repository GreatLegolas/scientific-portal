from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Review
from articles.models import Article
from .serializers import ReviewSerializer, ReviewCreateSerializer, AnonymousReviewSerializer

class ReviewListCreateView(generics.ListCreateAPIView):
    """API endpoint for listing and creating reviews"""
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ReviewCreateSerializer
        return ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.all()
        # Filter by article if specified
        article_id = self.request.query_params.get('article')
        if article_id:
            queryset = queryset.filter(article_id=article_id)
        # Filter by reviewer (for user's own reviews)
        if self.request.query_params.get('my_reviews'):
            queryset = queryset.filter(reviewer=self.request.user)
        return queryset

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for review details"""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Only allow reviewer to update their own reviews
        if serializer.instance.reviewer != self.request.user:
            raise permissions.PermissionDenied("You can only edit your own reviews.")
        serializer.save()

    def perform_destroy(self, instance):
        # Only allow reviewer to delete their own reviews
        if instance.reviewer != self.request.user:
            raise permissions.PermissionDenied("You can only delete your own reviews.")
        instance.delete()

class ArticleReviewsView(generics.ListAPIView):
    """API endpoint for article reviews (anonymous for authors)"""
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        article_id = self.kwargs.get('article_id')
        try:
            article = Article.objects.get(id=article_id)
            # If the user is the author, show anonymous reviews
            if article.author == self.request.user:
                return AnonymousReviewSerializer
        except Article.DoesNotExist:
            pass
        return ReviewSerializer

    def get_queryset(self):
        article_id = self.kwargs.get('article_id')
        return Review.objects.filter(article_id=article_id)

class MyReviewsView(generics.ListAPIView):
    """API endpoint for user's own reviews"""
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(reviewer=self.request.user)

