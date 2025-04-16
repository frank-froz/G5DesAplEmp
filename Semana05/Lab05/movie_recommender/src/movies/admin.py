from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Avg
from .models import Director, Actor, Genre, Movie, MovieActor, UserProfile, Rating
from .utils import create_recommendation_admin_action

class RuntimeFilter(admin.SimpleListFilter):
    """Filter movies by runtime range"""
    title = 'Runtime'
    parameter_name = 'runtime_range'
    
    def lookups(self, request, model_admin):
        return (
            ('short', 'Short (<90 min)'),
            ('medium', 'Medium (90-120 min)'),
            ('long', 'Long (>120 min)'),
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'short':
            return queryset.filter(runtime__lt=90)
        if self.value() == 'medium':
            return queryset.filter(runtime__gte=90, runtime__lte=120)
        if self.value() == 'long':
            return queryset.filter(runtime__gt=120)
        return queryset


# Inline for actors in a movie
class MovieActorInline(admin.TabularInline):
    """Inline admin for movie actors"""
    model = MovieActor
    extra = 1
    autocomplete_fields = ['actor']


# Inline for ratings
class RatingInline(admin.TabularInline):
    """Inline admin for ratings"""
    model = Rating
    extra = 0
    readonly_fields = ['user', 'value', 'created_at']
    can_delete = False
    max_num = 0  # Don't allow adding new ratings through admin


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    """Admin configuration for directors"""
    list_display = ('name', 'birth_date', 'movie_count')
    search_fields = ('name',)
    list_filter = ('birth_date',)
    date_hierarchy = 'birth_date'
    
    def movie_count(self, obj):
        """Count movies directed by this director"""
        count = obj.directed_movies.count()
        return count if count > 0 else '-'
    movie_count.short_description = "Movies Directed"


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Admin configuration for actors"""
    list_display = ('name', 'birth_date', 'movie_count')
    search_fields = ('name',)
    list_filter = ('birth_date',)
    
    def movie_count(self, obj):
        """Count movies this actor has appeared in"""
        count = obj.acted_in.count()
        return count if count > 0 else '-'
    movie_count.short_description = "Movies Appeared In"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Admin configuration for genres"""
    list_display = ('name', 'slug', 'movie_count')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    
    def movie_count(self, obj):
        """Count movies in this genre"""
        count = obj.movies.count()
        return count if count > 0 else '-'
    movie_count.short_description = "Movies"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Admin configuration for movies"""
    list_display = ('title', 'release_date', 'director', 'display_genres', 'avg_rating', 'display_poster')
    list_filter = ('genres', 'release_date', 'avg_rating', RuntimeFilter)
    search_fields = ('title', 'director__name', 'actors__name')
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ['director', 'genres']
    readonly_fields = ['display_poster', 'avg_rating']
    inlines = [MovieActorInline, RatingInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'release_date', 'director')
        }),
        ('Details', {
            'fields': ('plot', 'runtime', 'imdb_id', 'genres')
        }),
        ('Rating', {
            'fields': ('avg_rating',),
            'classes': ('collapse',)
        }),
        ('Poster', {
            'fields': ('poster', 'display_poster'),
            'classes': ('collapse',)
        }),
    )
    
    def display_genres(self, obj):
        """Display genres as a comma-separated list"""
        return ", ".join([genre.name for genre in obj.genres.all()])
    display_genres.short_description = "Genres"
    
    def display_poster(self, obj):
        """Display movie poster image"""
        if obj.poster:
            return format_html('<img src="{}" width="150" />', obj.poster.url)
        return "No poster available"
    display_poster.short_description = "Poster Preview"


@admin.register(MovieActor)
class MovieActorAdmin(admin.ModelAdmin):
    """Admin configuration for movie actors"""
    list_display = ('movie', 'actor', 'character_name', 'is_lead')
    list_filter = ('movie', 'actor', 'is_lead')
    search_fields = ('movie__title', 'actor__name', 'character_name')
    autocomplete_fields = ['movie', 'actor']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Admin configuration for user profiles"""
    list_display = ('user', 'favorite_genre_count', 'rating_count')
    search_fields = ('user__username',)
    filter_horizontal = ('favorite_genres', 'favorite_movies')
    
    def favorite_genre_count(self, obj):
        """Count favorite genres"""
        return obj.favorite_genres.count()
    favorite_genre_count.short_description = "Favorite Genres"
    
    def rating_count(self, obj):
        """Count ratings"""
        return obj.user.ratings.count()
    rating_count.short_description = "Ratings"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Admin configuration for ratings"""
    list_display = ('user', 'movie', 'value', 'created_at')
    list_filter = ('value', 'created_at')
    search_fields = ('user__username', 'movie__title')
    readonly_fields = ['created_at', 'updated_at']
    autocomplete_fields = ['user', 'movie']

class UserProfileAdmin(admin.ModelAdmin):
    """Admin configuration for user profiles"""
    list_display = ('user', 'favorite_genre_count', 'rating_count')
    search_fields = ('user__username',)
    filter_horizontal = ('favorite_genres', 'favorite_movies')
    actions = [create_recommendation_admin_action()]
    
    def favorite_genre_count(self, obj):
        """Count favorite genres"""
        return obj.favorite_genres.count()
    favorite_genre_count.short_description = "Favorite Genres"
    
    def rating_count(self, obj):
        """Count ratings"""
        return obj.user.ratings.count()
    rating_count.short_description = "Ratings"
