from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/', views.profile_view, name='profile'),  # 👈 Esta es la clave
        path('reading-list/', views.reading_list, name='reading_list'),  # agrega esta línea
    path('reading_list/create/', views.create_reading_list, name='create_reading_list'),
    path('reading_list/edit/<int:pk>/', views.edit_reading_list, name='edit_reading_list'),
    path('review/create/<int:book_id>/', views.create_review, name='create_review'),
    path('book-review/<int:book_id>/', views.book_review, name='book_review'),
    path('book-review/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('books/<int:book_id>/review/', views.book_review, name='book_review'),
]
