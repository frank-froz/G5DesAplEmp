from rest_framework import serializers
from .models import Category, Tag

class CategorySerializer(serializers.ModelSerializer):
    """Serializer for the Category model"""
    class Meta:
        model = Category
        fields = ['id', 'name']

class TagSerializer(serializers.ModelSerializer):
    """Serializer for the Tag model"""
    class Meta:
        model = Tag
        fields = ['id', 'name']
