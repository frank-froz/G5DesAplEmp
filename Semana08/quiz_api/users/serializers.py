from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, QuizAttempt
from quizzes.models import Quiz  # Asegúrate de importar el modelo Quiz

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'avatar', 'created_at']

class QuizAttemptSerializer(serializers.ModelSerializer):
    quiz = serializers.StringRelatedField()  # Muestra el título del quiz, o puedes usar un Serializer anidado.
    
    class Meta:
        model = QuizAttempt
        fields = ['user', 'quiz', 'score', 'max_score', 'completed_at']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    attempts = QuizAttemptSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile', 'attempts']
