from django.shortcuts import render, get_object_or_404
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    reviews = movie.reviews.all()
    
    user_review_exists = False
    if request.user.is_authenticated:
        user_review_exists = movie.reviews.filter(user=request.user).exists()
    
    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'reviews': reviews,
        'user_review_exists': user_review_exists,
    })
