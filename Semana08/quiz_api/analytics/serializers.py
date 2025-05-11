from rest_framework import serializers
from .models import QuestionStat, QuizActivity

class QuestionStatSerializer(serializers.ModelSerializer):
    """Serializador para el modelo QuestionStat"""
    class Meta:
        model = QuestionStat
        fields = ['question', 'attempts', 'correct_attempts', 'success_rate']

class QuizActivitySerializer(serializers.ModelSerializer):
    """Serializador para el modelo QuizActivity"""
    class Meta:
        model = QuizActivity
        fields = ['quiz', 'date', 'views', 'starts', 'completions']
