from django.contrib import admin
from .models import Author, AuthorProfile, Category, Publisher, Book, Publication

class AuthorProfileInline(admin.StackedInline):
    """Inline admin for author profiles"""
    model = AuthorProfile
    can_delete = False

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Admin configuration for authors"""
    list_display = ('name', 'birth_date')
    search_fields = ('name',)
    inlines = [AuthorProfileInline]

class PublicationInline(admin.TabularInline):
    """Inline admin for publications"""
    model = Publication
    extra = 1

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Admin configuration for books"""
    list_display = ('title', 'author', 'isbn', 'publication_date')
    list_filter = ('categories', 'author')
    search_fields = ('title', 'author__name', 'isbn')
    inlines = [PublicationInline]
    filter_horizontal = ('categories',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for categories"""
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    """Admin configuration for publishers"""
    list_display = ('name', 'website')
    search_fields = ('name',)

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    """Admin configuration for publications"""
    list_display = ('book', 'publisher', 'country', 'date_published')
    list_filter = ('publisher', 'country')
    search_fields = ('book__title', 'publisher__name', 'country')

