from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    """Category model for organizing articles"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Article(models.Model):
    """News article model"""
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to="articles/", blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    
    # Relationships
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    
    class Meta:
        ordering = ["-published_date"]
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("news:article_detail", kwargs={"slug": self.slug})