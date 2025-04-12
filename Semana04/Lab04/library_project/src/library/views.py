from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Author, Book, Category, Publisher

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

def book_detail(request, pk):
    """View for book details"""
    book = get_object_or_404(Book, pk=pk)
    # Get all categories for this book 🏷️
    categories = book.categories.all()
    # Get all publishers for this book with publication details 🏢
    publications = book.publication_set.select_related('publisher').all()
    
    context = {
        'book': book, 
        'categories': categories,
        'publications': publications
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
