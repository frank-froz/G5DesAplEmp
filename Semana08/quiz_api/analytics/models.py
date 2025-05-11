from django.db import models
from quizzes.models import Question, Quiz  

class QuestionStat(models.Model):
    """Modelo para hacer seguimiento de intentos y respuestas correctas de cada pregunta"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='stats')
    attempts = models.IntegerField(default=0)
    correct_attempts = models.IntegerField(default=0)

    @property
    def success_rate(self):
        """Calcular el porcentaje de respuestas correctas"""
        return (self.correct_attempts / self.attempts) * 100 if self.attempts > 0 else 0

    def __str__(self):
        return f"Stats for: {self.question.text[:30]}..."  # Mostrar un fragmento de la pregunta

class QuizActivity(models.Model):
    """Modelo para hacer seguimiento de la actividad de un cuestionario"""
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='activities')
    date = models.DateField(auto_now_add=True)  # Fecha en que se registró la actividad
    views = models.IntegerField(default=0)  # Número de vistas del cuestionario
    starts = models.IntegerField(default=0)  # Número de inicios del cuestionario
    completions = models.IntegerField(default=0)  # Número de completaciones del cuestionario

    class Meta:
        unique_together = ['quiz', 'date']  # Asegura que solo haya una entrada por día y cuestionario
    
    def __str__(self):
        return f"{self.quiz.title} activity on {self.date}"
