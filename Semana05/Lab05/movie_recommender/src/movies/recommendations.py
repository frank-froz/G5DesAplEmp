from django.db.models import Count, Q, Avg
from .models import Movie, Rating, UserProfile


def get_genre_recommendations(user, limit=5):
    """Get movie recommendations based on user's favorite genres"""
    
    # Get user's favorite genres from their profile
    try:
        favorite_genres = user.profile.favorite_genres.all()
    except UserProfile.DoesNotExist:
        return Movie.objects.none()
    
    if not favorite_genres:
        return Movie.objects.none()
    
    # Find movies in user's favorite genres that they haven't rated yet
    rated_movies = Rating.objects.filter(user=user).values_list('movie_id', flat=True)
    
    recommendations = (
        Movie.objects
        .filter(genres__in=favorite_genres)
        .exclude(id__in=rated_movies)
        .annotate(relevance=Count('genres', filter=Q(genres__in=favorite_genres)))
        .order_by('-avg_rating', '-relevance', '-release_date')[:limit]
    )
    
    return recommendations


def get_collaborative_recommendations(user, limit=5):
    """Get movie recommendations based on similar users' ratings"""
    
    # Get movies that the user has rated highly (7+)
    user_ratings = Rating.objects.filter(user=user, value__gte=7)
    
    if not user_ratings.exists():
        return Movie.objects.none()
    
    # Find users who rated the same movies highly
    similar_users = (
        Rating.objects
        .filter(movie__in=user_ratings.values('movie'), value__gte=7)
        .exclude(user=user)
        .values('user')
        .annotate(common_count=Count('user'))
        .filter(common_count__gte=1)  # At least 1 movie in common
        .values_list('user', flat=True)
    )
    
    if not similar_users:
        return Movie.objects.none()
    
    # Get movies that similar users rated highly but the user hasn't rated yet
    rated_movies = user_ratings.values_list('movie', flat=True)
    
    recommendations = (
        Movie.objects
        .filter(ratings__user__in=similar_users, ratings__value__gte=8)
        .exclude(id__in=rated_movies)
        .annotate(avg_similar_rating=Avg('ratings__value', filter=Q(ratings__user__in=similar_users)))
        .order_by('-avg_similar_rating', '-avg_rating')[:limit]
    )
    
    return recommendations


def get_recommendations(user, limit=10):
    """Get combined recommendations for a user"""
    
    # Get genre-based recommendations
    genre_recs = list(get_genre_recommendations(user, limit=limit//2))
    
    # Get collaborative recommendations
    collab_recs = list(get_collaborative_recommendations(user, limit=limit//2))
    
    # Combine recommendations (avoid duplicates)
    all_recs = genre_recs.copy()
    
    # Add collaborative recommendations if they're not already in the list
    movie_ids = {movie.id for movie in all_recs}
    for movie in collab_recs:
        if movie.id not in movie_ids:
            all_recs.append(movie)
            movie_ids.add(movie.id)
    
    # Limit to requested number
    return all_recs[:limit]
