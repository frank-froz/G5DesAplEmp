from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Category, Tag
from .serializers import CategorySerializer, TagSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for Category model"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagViewSet(viewsets.ModelViewSet):
    """ViewSet for Tag model"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
