from django.db import models
from django.utils.text import slugify

class Author(models.Model):
    """Model representing an author of books"""
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    biography = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class AuthorProfile(models.Model):
    """One-to-one model with additional author information"""
    author = models.OneToOneField(  # 1️⃣➡️1️⃣ One-to-One relationship
        Author, 
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile'
    )
    website = models.URLField(blank=True)
    twitter_handle = models.CharField(max_length=50, blank=True)
    photo = models.ImageField(upload_to='author_photos/', blank=True)
    
    def __str__(self):
        return f"Profile for {self.author.name}"

class Category(models.Model):
    """Model representing a book category/genre"""
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = "categories"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Publisher(models.Model):
    """Model representing a book publisher"""
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    """Model representing a book with multiple relationships"""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(  # 1️⃣➡️🔢 One-to-Many relationship
        Author, 
        on_delete=models.CASCADE,
        related_name='books'
    )
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    publication_date = models.DateField(null=True, blank=True)
    summary = models.TextField(blank=True)
    # 🔢➡️🔢 Many-to-Many relationship with Category
    categories = models.ManyToManyField(
        Category,
        related_name='books'
    )
    # 🔢🔗🔢 Many-to-Many relationship with Publisher through Publication
    publishers = models.ManyToManyField(
        Publisher,
        through='Publication',
        through_fields=('book', 'publisher'),
        related_name='books'
    )
    
    def __str__(self):
        return self.title

class Publication(models.Model):
    """Intermediate model for the many-to-many relationship
    between books and publishers"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    date_published = models.DateField()
    country = models.CharField(max_length=50)
    
    class Meta:
        unique_together = ('book', 'publisher', 'country')
    
    def __str__(self):
        return f"{self.book.title} published by {self.publisher.name} in {self.country}"
