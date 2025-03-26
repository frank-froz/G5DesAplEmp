from django.db import models

# Definición de la clase Task que hereda de models.Model
class Task(models.Model):
    # Opciones para el campo priority
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    # Opciones para el campo status
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    # Campos del modelo:
    title = models.CharField(max_length=200)  # Título de la tarea
    description = models.TextField(blank=True)  # Descripción (opcional)
    created_date = models.DateTimeField(auto_now_add=True)  # Fecha creación (automática)
    due_date = models.DateField(null=True, blank=True)  # Fecha vencimiento (opcional)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium'
    )  # Prioridad con valor por defecto
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='pending'
    )  # Estado con valor por defecto
    
    # Método para representación string del objeto
    def __str__(self):
        return self.title
        
    # Clase Meta para metadatos adicionales
    class Meta:
        ordering = ['-created_date']  # Orden por defecto (más reciente primero)