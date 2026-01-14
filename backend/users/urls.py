from django.urls import path
from .views import (
    UserRegistrationView,
    UserProfileView,
    UserDetailView,
    UserStatsView,
)

app_name = 'users'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('stats/', UserStatsView.as_view(), name='stats'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
