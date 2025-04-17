from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from movies.models import Movie
from django.contrib.auth.decorators import login_required

# Listar reseñas de una película
def movie_reviews(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.reviews.all()
    return render(request, 'reviews/movie_reviews.html', {'movie': movie, 'reviews': reviews})

# Crear nueva reseña
@login_required
def add_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        rating = int(request.POST['rating'])

        Review.objects.create(
            movie=movie,
            user=request.user,
            title=title,
            content=content,
            rating=rating
        )
        return redirect('movie_reviews', movie_id=movie.id)

    return render(request, 'reviews/add_review.html', {'movie': movie})
