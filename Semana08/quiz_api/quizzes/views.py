from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Quiz, Question, Choice
from .serializers import (
    QuizSerializer, QuizDetailSerializer,
    QuestionSerializer, QuestionDetailSerializer,
    ChoiceSerializer, AnswerSerializer
)


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
        
        # Validate incoming data
        serializer = AnswerSerializer(data=request.data.get('answers', []), many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Process answers
        answers = serializer.validated_data
        results = []
        
        for answer in answers:
            question_id = answer['question_id']
            choice_id = answer['choice_id']
            
            try:
                # Check if question belongs to this quiz
                question = Question.objects.get(id=question_id, quiz=quiz)
                
                # Check if choice belongs to this question
                choice = Choice.objects.get(id=choice_id, question=question)
                
                # Add result for this answer
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
        
        # Calculate score
        correct_answers = sum(1 for r in results if r.get('correct', False))
        total_answers = len(results)
        
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