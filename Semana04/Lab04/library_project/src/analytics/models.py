from django.db import models
from library.models import Book, Author, Category, Publisher
from users.models import LibraryUser

class BookView(models.Model):
    """Model to track book page views"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='views')
    user = models.ForeignKey(LibraryUser, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"View of {self.book.title}"

class CategoryAnalytics(models.Model):
    """Model to store aggregated category analytics"""
    category = models.OneToOneField(Category, on_delete=models.CASCADE, related_name='analytics')
    total_views = models.PositiveIntegerField(default=0)
    total_books = models.PositiveIntegerField(default=0)
    popularity_score = models.FloatField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Analytics for {self.category.name}"

class AuthorAnalytics(models.Model):
    """Model to store aggregated author analytics"""
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='analytics')
    total_views = models.PositiveIntegerField(default=0)
    avg_rating = models.FloatField(default=0)
    total_reviews = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Analytics for {self.author.name}"

class RecommendationLog(models.Model):
    """Model to log book recommendations"""
    user = models.ForeignKey(LibraryUser, on_delete=models.CASCADE, related_name='recommendations')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    clicked = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Recommendation of {self.book.title} to {self.user.username}"
