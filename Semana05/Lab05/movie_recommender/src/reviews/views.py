from django.shortcuts import render, get_object_or_404, redirect
from reviews.forms import ReviewForm
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
    movie = get_object_or_404(Movie, pk=movie_id)

    # Verificar si el usuario ya ha dejado una reseña para esta película
    user_review_exists = movie.reviews.filter(user=request.user).exists()

    if user_review_exists:
        return redirect('movie_detail', pk=movie_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            return redirect('movie_detail', pk=movie.id)
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form, 'movie': movie, 'user_review_exists': user_review_exists})

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', pk=review.movie.id)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/edit_review.html', {'form': form, 'review': review})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)

    if request.method == 'POST':
        movie_id = review.movie.id
        review.delete()
        return redirect('movie_detail', pk=movie_id)

    return render(request, 'reviews/delete_review.html', {'review': review})