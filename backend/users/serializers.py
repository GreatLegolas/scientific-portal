from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """Serializer for user details"""
    articles_count = serializers.SerializerMethodField()
    reviews_given_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'email_verified', 'orcid_id', 
                  'bio', 'affiliation', 'created_at', 'articles_count', 
                  'reviews_given_count']
        read_only_fields = ['id', 'created_at', 'email_verified']

    def get_articles_count(self, obj):
        return obj.articles.count()

    def get_reviews_given_count(self, obj):
        return obj.reviews_given.count()

class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'bio', 'affiliation']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
