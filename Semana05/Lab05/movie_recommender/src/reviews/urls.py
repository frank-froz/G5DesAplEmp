from django.urls import path
from . import views

urlpatterns = [
    path('movie/<int:movie_id>/reviews/', views.movie_reviews, name='movie_reviews'),
    path('movie/<int:movie_id>/reviews/add/', views.add_review, name='add_review'),
    path('add/<int:movie_id>/', views.add_review, name='add_review'),
    path('add_review/<int:movie_id>/', views.add_review, name='add_review'),
    path('edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
]
