from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Article
from .serializers import ArticleSerializer, ArticleDetailSerializer, ArticleSubmitSerializer

class ArticleListCreateView(generics.ListCreateAPIView):
    """API endpoint for listing and creating articles"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Article.objects.all()
        # Filter by author if specified
        author_id = self.request.query_params.get('author')
        if author_id:
            queryset = queryset.filter(author_id=author_id)
        # Filter by status if specified
        status_filter = self.request.query_params.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset

class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for article details"""
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Increment view count
        instance.view_count += 1
        instance.save(update_fields=['view_count'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_update(self, serializer):
        # Only allow author to update their own articles
        if serializer.instance.author != self.request.user:
            raise permissions.PermissionDenied("You can only edit your own articles.")
        serializer.save()

    def perform_destroy(self, instance):
        # Only allow author to delete their own articles
        if instance.author != self.request.user:
            raise permissions.PermissionDenied("You can only delete your own articles.")
        instance.delete()

class MyArticlesView(generics.ListAPIView):
    """API endpoint for user's own articles"""
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def submit_article(request):
    """API endpoint for submitting a new article"""
    serializer = ArticleSubmitSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        article = serializer.save()
        return Response(
            ArticleSerializer(article).data,
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

