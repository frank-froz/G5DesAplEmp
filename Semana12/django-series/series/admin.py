from django.contrib import admin
from .models import Serie, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ('id', 'cod', 'nom', 'cat', 'img')
    search_fields = ('nom',)
    list_filter = ('cat',)
