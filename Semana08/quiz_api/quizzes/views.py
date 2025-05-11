from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Quiz, Question, Choice
from analytics.models import QuizActivity, QuestionStat  # Asegúrate de importar QuizActivity
from .serializers import (
    QuizSerializer, QuizDetailSerializer,
    QuestionSerializer, QuestionDetailSerializer,
    ChoiceSerializer, AnswerSerializer
)
from datetime import date

class QuizViewSet(viewsets.ModelViewSet):
    """ViewSet for Quiz model"""
    queryset = Quiz.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return QuizDetailSerializer
        return QuizSerializer
    
    @action(detail=True, methods=['post'])
    def validate(self, request, pk=None):
        """Validate answers for a specific quiz"""
        quiz = self.get_object()
        
        # Validar los datos de las respuestas
        serializer = AnswerSerializer(data=request.data.get('answers', []), many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Procesar las respuestas
        answers = serializer.validated_data
        results = []
        
        for answer in answers:
            question_id = answer['question_id']
            choice_id = answer['choice_id']
            
            try:
                # Verificar si la pregunta pertenece a este cuestionario
                question = Question.objects.get(id=question_id, quiz=quiz)
                
                # Verificar si la opción pertenece a esta pregunta
                choice = Choice.objects.get(id=choice_id, question=question)
                
                # Actualizar estadísticas de la pregunta
                question_stat, created = QuestionStat.objects.get_or_create(question=question)
                question_stat.attempts += 1
                if choice.is_correct:
                    # Incrementar respuestas correctas si la opción seleccionada es correcta
                    question_stat.correct_attempts += 1
                question_stat.save()
                
                # Agregar el resultado de esta respuesta
                results.append({
                    'question_id': question_id,
                    'correct': choice.is_correct,
                    'correct_choice': Choice.objects.filter(
                        question=question, is_correct=True
                    ).first().id if not choice.is_correct else None
                })
                
            except (Question.DoesNotExist, Choice.DoesNotExist):
                results.append({
                    'question_id': question_id,
                    'error': 'Question or choice not found'
                })
        
        # Calcular el puntaje
        correct_answers = sum(1 for r in results if r.get('correct', False))
        total_answers = len(results)
        
        # Actualizar la actividad del cuestionario: incrementar completaciones
        activity, created = QuizActivity.objects.get_or_create(quiz=quiz, date=date.today())
        activity.completions += 1  # Incrementar las completaciones
        activity.save()

        return Response({
            'quiz_id': quiz.id,
            'score': f"{correct_answers}/{total_answers}",
            'percentage': int((correct_answers / total_answers) * 100) if total_answers else 0,
            'results': results
        })


class QuestionViewSet(viewsets.ModelViewSet):
    """ViewSet for Question model"""
    queryset = Question.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return QuestionDetailSerializer
        return QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    """ViewSet for Choice model"""
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer