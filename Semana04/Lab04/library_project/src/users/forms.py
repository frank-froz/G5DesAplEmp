# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from library.models import Book
from .models import LibraryUser, ReadingList, BookReview

class LibraryUserCreationForm(UserCreationForm):
    class Meta:
        model = LibraryUser
        fields = ['username', 'email', 'bio', 'favorite_categories', 'profile_image']

class LibraryUserChangeForm(UserChangeForm):
    class Meta:
        model = LibraryUser
        fields = ['username', 'email', 'bio', 'favorite_categories', 'profile_image']

class ReadingListForm(forms.ModelForm):
    """Formulario para crear o editar una lista de lectura"""
    class Meta:
        model = ReadingList
        fields = ['name', 'description', 'books', 'is_public']

    books = forms.ModelMultipleChoiceField(queryset=Book.objects.all(), widget=forms.CheckboxSelectMultiple)

class BookReviewForm(forms.ModelForm):
    """Formulario para crear o editar una reseña de un libro"""
    class Meta:
        model = BookReview
        fields = ['rating', 'comment']