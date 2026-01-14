from django.urls import path
from .views import (
    ArticleListCreateView,
    ArticleDetailView,
    MyArticlesView,
    submit_article,
)

app_name = 'articles'

urlpatterns = [
    path('', ArticleListCreateView.as_view(), name='article-list'),
    path('my-articles/', MyArticlesView.as_view(), name='my-articles'),
    path('submit/', submit_article, name='submit-article'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]
