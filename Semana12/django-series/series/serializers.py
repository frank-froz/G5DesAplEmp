from rest_framework import serializers
from .models import Serie, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']

class SerieSerializer(serializers.ModelSerializer):
    # Para escritura (POST/PUT) con solo el ID de categoría
    cat = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    # Para lectura (GET) con detalle completo de la categoría
    cat_detail = CategoriaSerializer(source='cat', read_only=True)

    class Meta:
        model = Serie
        fields = ['id', 'cod', 'nom', 'cat', 'cat_detail', 'img']
