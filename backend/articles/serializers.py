from rest_framework import serializers
from .models import Article
from django.utils import timezone

class ArticleSerializer(serializers.ModelSerializer):
    """Serializer for articles"""
    author_name = serializers.CharField(source='author.username', read_only=True)
    keywords_list = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'abstract', 'keywords', 'keywords_list', 
                  'author', 'author_name', 'status', 'view_count', 
                  'created_at', 'updated_at', 'submitted_at', 'reviews_count']
        read_only_fields = ['id', 'author', 'view_count', 'created_at', 'updated_at']

    def get_keywords_list(self, obj):
        return obj.get_keywords_list()

    def get_reviews_count(self, obj):
        return obj.reviews.count()

    def create(self, validated_data):
        # Set the author to the current user
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

class ArticleDetailSerializer(ArticleSerializer):
    """Detailed serializer for single article view"""
    pass

class ArticleSubmitSerializer(serializers.ModelSerializer):
    """Serializer for submitting an article"""
    class Meta:
        model = Article
        fields = ['title', 'abstract', 'keywords']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        validated_data['status'] = 'submitted'
        validated_data['submitted_at'] = timezone.now()
        return super().create(validated_data)
