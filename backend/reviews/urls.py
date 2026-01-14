from django.urls import path
from .views import (
    ReviewListCreateView,
    ReviewDetailView,
    ArticleReviewsView,
    MyReviewsView,
)

app_name = 'reviews'

urlpatterns = [
    path('', ReviewListCreateView.as_view(), name='review-list'),
    path('my-reviews/', MyReviewsView.as_view(), name='my-reviews'),
    path('article/<int:article_id>/', ArticleReviewsView.as_view(), name='article-reviews'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]
