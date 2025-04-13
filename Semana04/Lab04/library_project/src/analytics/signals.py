from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BookView, CategoryAnalytics
from library.models import Book

@receiver(post_save, sender=BookView)
def update_category_analytics(sender, instance, created, **kwargs):
    """Actualizar las estadísticas de categoría cuando se registre una nueva vista de libro"""
    if created:
        # Obtén la categoría del libro
        categories = instance.book.categories.all()
        
        # Actualiza las estadísticas de cada categoría asociada al libro
        for category in categories:
            category_analytics, created = CategoryAnalytics.objects.get_or_create(category=category)
            
            # Incrementar el total de vistas
            category_analytics.total_views += 1
            category_analytics.save()
            
            # Actualizar el score de popularidad
            category_analytics.update_popularity_score()
