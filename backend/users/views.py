from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserRegistrationSerializer

User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    """API endpoint for user registration"""
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        return Response({
            'user': UserSerializer(user).data,
            'message': 'User registered successfully. Email verification is pending.'
        }, status=status.HTTP_201_CREATED)

class UserProfileView(generics.RetrieveUpdateAPIView):
    """API endpoint for user profile"""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserDetailView(generics.RetrieveAPIView):
    """API endpoint for viewing user details"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserStatsView(APIView):
    """API endpoint for user statistics"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        stats = {
            'articles_authored': user.articles.count(),
            'articles_published': user.articles.filter(status='published').count(),
            'reviews_given': user.reviews_given.count(),
            'reviews_completed': user.reviews_given.filter(status='completed').count(),
            'total_article_views': sum(article.view_count for article in user.articles.all()),
            'articles_under_review': user.articles.filter(status='under_review').count(),
        }
        return Response(stats)

