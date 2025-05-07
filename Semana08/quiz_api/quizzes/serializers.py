from rest_framework import serializers
from .models import Quiz, Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    """Serializer for the Choice model"""
    class Meta:
        model = Choice
        fields = ['id', 'text', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    """Serializer for the Question model"""
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'text']


class QuestionDetailSerializer(serializers.ModelSerializer):
    """Serializer for Question model with nested choices"""
    choices = ChoiceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'text', 'choices']


class QuizSerializer(serializers.ModelSerializer):
    """Serializer for the Quiz model"""
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at']


class QuizDetailSerializer(serializers.ModelSerializer):
    """Serializer for Quiz model with nested questions and choices"""
    questions = serializers.SerializerMethodField()
    
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at', 'questions']
    
    def get_questions(self, obj):
        questions = obj.questions.all()
        return QuestionDetailSerializer(questions, many=True).data


class AnswerSerializer(serializers.Serializer):
    """Serializer for answer validation"""
    question_id = serializers.IntegerField()
    choice_id = serializers.IntegerField()