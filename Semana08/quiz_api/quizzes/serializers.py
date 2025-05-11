from rest_framework import serializers
from .models import Quiz, Question, Choice
from categories.models import Category, Tag
from categories.serializers import CategorySerializer, TagSerializer


class ChoiceSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Choice"""
    question = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all()
    )

    class Meta:
        model = Choice
        fields = ['id', 'text', 'is_correct', 'question']


class QuestionSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Question"""
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'text']


class QuestionDetailSerializer(serializers.ModelSerializer):
    """Serializer para Question con sus Choice anidados"""
    choices = ChoiceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'text', 'choices']


class QuizSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Quiz (lista/creación)"""
    # relacionar categoria y etiquetas por su ID
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        allow_null=True,
        required=False
    )
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Quiz
        fields = [
            'id',
            'title',
            'description',
            'category',   # campo para asignar categoría
            'tags',       # campo para asignar etiquetas
            'created_at',
            'updated_at',
        ]


class QuizDetailSerializer(serializers.ModelSerializer):
    """Serializer para Quiz con preguntas, choices, categoría y etiquetas anidadas"""
    category = CategorySerializer(read_only=True)  # muestro datos completos de la categoría
    tags = TagSerializer(many=True, read_only=True)  # muestro datos completos de las etiquetas
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = [
            'id',
            'title',
            'description',
            'category',    # categoría anidada
            'tags',        # etiquetas anidadas
            'created_at',
            'updated_at',
            'questions',   # preguntas anidadas
        ]
    
    def get_questions(self, obj):
        questions = obj.questions.all()
        return QuestionDetailSerializer(questions, many=True).data


class AnswerSerializer(serializers.Serializer):
    """Serializer para validar respuestas"""
    question_id = serializers.IntegerField()
    choice_id = serializers.IntegerField()
