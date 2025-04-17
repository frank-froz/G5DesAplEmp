from django.urls import path
from . import views

urlpatterns = [
    path('movie/<int:movie_id>/reviews/', views.movie_reviews, name='movie_reviews'),
    path('movie/<int:movie_id>/reviews/add/', views.add_review, name='add_review'),
]
