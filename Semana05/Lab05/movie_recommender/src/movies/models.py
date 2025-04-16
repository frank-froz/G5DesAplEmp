from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Person(models.Model):
    """Base model for people in the movie industry"""
    name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    biography = models.TextField(blank=True)
    photo = models.ImageField(upload_to='people/', blank=True)
    
    class Meta:
        verbose_name_plural = "people"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Director(Person):
    """Director model inheriting from Person"""
    awards = models.TextField(blank=True, help_text="List of awards won")
    
    def __str__(self):
        return f"Director: {self.name}"


class Actor(Person):
    """Actor model inheriting from Person"""
    awards = models.TextField(blank=True, help_text="List of awards won")
    
    def __str__(self):
        return f"Actor: {self.name}"


class Genre(models.Model):
    """Movie genre"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['name']


class Movie(models.Model):
    """Movie model with various relationships"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    release_date = models.DateField(null=True, blank=True)
    poster = models.ImageField(upload_to='posters/', blank=True)
    plot = models.TextField(blank=True)
    runtime = models.PositiveIntegerField(help_text="Runtime in minutes", null=True, blank=True)
    imdb_id = models.CharField("IMDb ID", max_length=20, blank=True)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    
    # One-to-Many: One director can direct many movies
    director = models.ForeignKey(
        Director,
        on_delete=models.SET_NULL,
        related_name='directed_movies',
        null=True,
        blank=True
    )
    
    # Many-to-Many: Movies have many genres, genres have many movies
    genres = models.ManyToManyField(
        Genre,
        related_name='movies'
    )
    
    # Many-to-Many: Movies have many actors, actors appear in many movies
    actors = models.ManyToManyField(
        Actor,
        through='MovieActor',
        related_name='acted_in'
    )
    
    class Meta:
        ordering = ['-release_date', 'title']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def update_avg_rating(self):
        """Update the average rating for this movie"""
        ratings = self.ratings.all()
        if ratings.exists():
            total = sum(r.value for r in ratings)
            self.avg_rating = total / ratings.count()
        else:
            self.avg_rating = 0
        self.save()


class MovieActor(models.Model):
    """Intermediate model for Movie-Actor many-to-many relationship"""
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    character_name = models.CharField(max_length=200)
    is_lead = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('movie', 'actor', 'character_name')
        verbose_name = "Movie Actor"
        verbose_name_plural = "Movie Actors"
    
    def __str__(self):
        return f"{self.actor.name} as {self.character_name} in {self.movie.title}"


class UserProfile(models.Model):
    """Extended user information"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    favorite_genres = models.ManyToManyField(Genre, blank=True, related_name='fans')
    favorite_movies = models.ManyToManyField(Movie, blank=True, related_name='fans')
    
    def __str__(self):
        return f"Profile for {self.user.username}"


class Rating(models.Model):
    """Movie ratings by users"""
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    value = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Rating from 1 to 10"
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('movie', 'user')
    
    def __str__(self):
        return f"{self.user.username} rated {self.movie.title}: {self.value}/10"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update movie's average rating
        self.movie.update_avg_rating()
