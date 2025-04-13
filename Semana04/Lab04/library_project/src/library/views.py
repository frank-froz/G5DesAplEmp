from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Author, Book, Category, Publisher
from analytics.models import BookView, CategoryAnalytics

def home(request):
    """View for home page with library statistics"""
    context = {
        'total_books': Book.objects.count(),
        'total_authors': Author.objects.count(),
        'total_categories': Category.objects.count(),
        'total_publishers': Publisher.objects.count(),
        # Get categories with book counts 📊
        'categories': Category.objects.annotate(
            book_count=Count('books')
        ).order_by('-book_count')[:5],
        # Get recent books 📚
        'recent_books': Book.objects.select_related('author').order_by('-publication_date')[:5],
    }
    return render(request, 'library/home.html', context)

def author_list(request):
    """View for listing all authors"""
    authors = Author.objects.all().order_by('name')
    return render(request, 'library/author_list.html', {'authors': authors})

def author_detail(request, pk):
    """View for author details with books"""
    author = get_object_or_404(Author, pk=pk)
    # Get all books by this author 📚
    books = author.books.all()
    return render(request, 'library/author_detail.html', {'author': author, 'books': books})

def book_list(request):
    """View for listing all books"""
    books = Book.objects.all().select_related('author').order_by('title')
    return render(request, 'library/book_list.html', {'books': books})

from analytics.models import BookView  # 👈 Importa esto arriba

# views.py
from django.shortcuts import render, get_object_or_404
from .models import Book
from analytics.models import BookView  # Importar el modelo BookView
import logging

logger = logging.getLogger(__name__)  # Para poder registrar los logs

def book_detail(request, pk):
    """Vista para los detalles del libro"""
    book = get_object_or_404(Book, pk=pk)
    
    # Crear una entrada para la vista de este libro
    book_view = BookView.objects.create(book=book, user=request.user if request.user.is_authenticated else None)
    
    # Log para verificar que el objeto BookView se ha creado
    logger.debug(f"BookView created: {book_view}")
    
    # Obtener todas las categorías para este libro
    categories = book.categories.all()

    # Obtener todas las publicaciones para este libro
    publications = book.publication_set.select_related('publisher').all()
    
    # Obtener todas las reseñas asociadas a este libro
    reviews = book.reviews.all()

    # Obtener el total de vistas para este libro
    total_views = BookView.objects.filter(book=book).count()

    # Obtener las estadísticas de categoría para las categorías asociadas al libro
    category_analytics = CategoryAnalytics.objects.filter(category__in=categories)
    
    context = {
        'book': book, 
        'categories': categories,
        'total_views': total_views,  # Añadir el total de vistas al contexto
        'publications': publications,
        'reviews': reviews,
        'category_analytics': category_analytics,  # Añadir las estadísticas de categoría al contexto
    }
    
    return render(request, 'library/book_detail.html', context)



def category_list(request):
    """View for listing all categories"""
    categories = Category.objects.annotate(book_count=Count('books')).order_by('name')
    return render(request, 'library/category_list.html', {'categories': categories})

def category_detail(request, slug):
    """View for category details with books"""
    category = get_object_or_404(Category, slug=slug)
    # Get all books in this category 📚
    books = category.books.all().select_related('author')
    return render(request, 'library/category_detail.html', {'category': category, 'books': books})
