from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Serie(models.Model):
    cod = models.IntegerField(unique=True)
    nom = models.CharField(max_length=100)
    cat = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='series')
    img = models.ImageField(upload_to='series/', blank=True, null=True)
    

    def __str__(self):
        return self.nom


