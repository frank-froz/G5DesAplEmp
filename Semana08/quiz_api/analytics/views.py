from rest_framework import viewsets
from .models import QuestionStat, QuizActivity
from .serializers import QuestionStatSerializer, QuizActivitySerializer

class QuestionStatViewSet(viewsets.ModelViewSet):
    """ViewSet para obtener estadísticas de las preguntas"""
    queryset = QuestionStat.objects.all()
    serializer_class = QuestionStatSerializer

class QuizActivityViewSet(viewsets.ModelViewSet):
    """ViewSet para obtener la actividad de los cuestionarios"""
    queryset = QuizActivity.objects.all()
    serializer_class = QuizActivitySerializer
