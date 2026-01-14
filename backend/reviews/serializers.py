from rest_framework import serializers
from .models import Review
from django.utils import timezone

class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for reviews"""
    article_title = serializers.CharField(source='article.title', read_only=True)
    reviewer_name = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'article', 'article_title', 'reviewer', 'reviewer_name',
                  'status', 'recommendation', 'comments', 'confidential_comments',
                  'created_at', 'updated_at', 'completed_at']
        read_only_fields = ['id', 'reviewer', 'created_at', 'updated_at']

    def get_reviewer_name(self, obj):
        # Return anonymous for authors, actual name for reviewers/admins
        request = self.context.get('request')
        if request and request.user == obj.reviewer:
            return obj.reviewer.username
        return "Anonymous Reviewer"

class ReviewCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a review"""
    class Meta:
        model = Review
        fields = ['article', 'comments', 'confidential_comments', 'recommendation']

    def create(self, validated_data):
        validated_data['reviewer'] = self.context['request'].user
        if validated_data.get('recommendation'):
            validated_data['status'] = 'completed'
            validated_data['completed_at'] = timezone.now()
        return super().create(validated_data)

class AnonymousReviewSerializer(serializers.ModelSerializer):
    """Serializer for anonymous review display (for authors)"""
    class Meta:
        model = Review
        fields = ['id', 'status', 'recommendation', 'comments', 'created_at', 'completed_at']
        read_only_fields = ['id', 'status', 'recommendation', 'comments', 'created_at', 'completed_at']
