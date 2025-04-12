# users/views.py
from django.shortcuts import get_object_or_404, render, redirect
from .forms import LibraryUserCreationForm, LibraryUserChangeForm, ReadingListForm, BookReviewForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import ReadingList, Book, BookReview
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = LibraryUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirige a la página principal o a otra vista que elijas
    else:
        form = LibraryUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def edit_profile(request):
    if request.method == 'POST':
        form = LibraryUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige a la página del perfil del usuario
    else:
        form = LibraryUserChangeForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})

def reading_list(request):
    """Vista para mostrar todas las listas de lectura de un usuario"""
    reading_lists = request.user.reading_lists.all()
    return render(request, 'users/reading_list.html', {'reading_lists': reading_lists})


def reading_list_detail(request, id):
    """Vista para mostrar los detalles de una lista de lectura"""
    reading_list = get_object_or_404(ReadingList, id=id, user=request.user)
    return render(request, 'users/reading_list_detail.html', {'reading_list': reading_list})


@login_required
def create_reading_list(request):
    """Vista para crear una lista de lectura"""
    if request.method == 'POST':
        form = ReadingListForm(request.POST)
        if form.is_valid():
            reading_list = form.save(commit=False)
            reading_list.user = request.user  # Asignar el usuario actual
            reading_list.save()
            return redirect('profile')  # Redirige al perfil del usuario
    else:
        form = ReadingListForm()
    
    return render(request, 'users/create_reading_list.html', {'form': form})

@login_required
def edit_reading_list(request, pk):
    """Vista para editar una lista de lectura existente"""
    reading_list = ReadingList.objects.get(pk=pk)
    if reading_list.user != request.user:
        return redirect('profile')  # Si el usuario no es el dueño, redirige al perfil
    
    if request.method == 'POST':
        form = ReadingListForm(request.POST, instance=reading_list)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige al perfil del usuario
    else:
        form = ReadingListForm(instance=reading_list)
    
    return render(request, 'users/edit_reading_list.html', {'form': form, 'reading_list': reading_list})


@login_required
def create_review(request, book_id):
    """Vista para crear una reseña de un libro"""
    book = Book.objects.get(id=book_id)
    
    if request.method == 'POST':
        form = BookReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # Asignar el usuario actual
            review.book = book  # Asignar el libro correspondiente
            review.save()
            return redirect('book_detail', pk=book.id)  # Redirige a la página de detalles del libro
    else:
        form = BookReviewForm()
    
    return render(request, 'users/create_review.html', {'form': form, 'book': book})

from django.contrib import messages

def book_review(request, book_id):
    """Vista para agregar una reseña a un libro"""
    book = get_object_or_404(Book, id=book_id)
    
    # Verificar si el usuario ya ha reseñado este libro
    if book.reviews.filter(user=request.user).exists():
        messages.error(request, "Ya has dejado una reseña para este libro.")
        return redirect('book_detail', pk=book.id)
    
    if request.method == 'POST':
        form = BookReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            return redirect('book_detail', pk=book.id)  # Redirige a la página del libro después de agregar la reseña
    else:
        form = BookReviewForm()

    return render(request, 'users/book_review.html', {'form': form, 'book': book})


def edit_review(request, review_id):
    """Vista para editar una reseña existente"""
    review = get_object_or_404(BookReview, id=review_id, user=request.user)
    if request.method == 'POST':
        form = BookReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=review.book.id)  # Redirige a la página del libro después de editar la reseña
    else:
        form = BookReviewForm(instance=review)
    return render(request, 'users/edit_review.html', {'form': form, 'review': review})