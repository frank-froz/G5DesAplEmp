from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.forms import inlineformset_factory
from django.db import transaction
from .models import Exam, Question, Choice
from .forms import ExamForm, QuestionForm, ChoiceFormSet

def exam_list(request):
    """Vista para listar todos los exámenes"""
    exams = Exam.objects.all().order_by('-created_date')
    return render(request, 'quiz/exam_list.html', {'exams': exams})

def exam_detail(request, exam_id):
    """Vista para mostrar el detalle de un examen con sus preguntas"""
    exam = get_object_or_404(Exam, id=exam_id)
    questions = exam.questions.all().prefetch_related('choices')
    return render(request, 'quiz/exam_detail.html', {'exam': exam, 'questions': questions})

def exam_create(request):
    """Vista para crear un nuevo examen"""
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save()
            messages.success(request, 'Examen creado correctamente.')
            return redirect('question_create', exam_id=exam.id)
    else:
        form = ExamForm()
    
    return render(request, 'quiz/exam_form.html', {'form': form})

def question_create(request, exam_id):
    """Vista para añadir preguntas a un examen"""
    exam = get_object_or_404(Exam, id=exam_id)
    
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        
        if question_form.is_valid():
            with transaction.atomic():
                # Guardar la pregunta
                question = question_form.save(commit=False)
                question.exam = exam
                question.save()
                
                # Procesar el formset para las opciones
                formset = ChoiceFormSet(request.POST, instance=question)
                if formset.is_valid():
                    formset.save()
                    
                    # Verificar que solo una opción sea marcada como correcta
                    correct_count = question.choices.filter(is_correct=True).count()
                    if correct_count != 1:
                        messages.warning(request, 'Debe haber exactamente una respuesta correcta.')
                    else:
                        messages.success(request, 'Pregunta añadida correctamente.')
                        
                    # Decidir a dónde redirigir
                    if 'add_another' in request.POST:
                        return redirect('question_create', exam_id=exam.id)
                    else:
                        return redirect('exam_detail', exam_id=exam.id)
    else:
        question_form = QuestionForm()
        formset = ChoiceFormSet()
    
    return render(request, 'quiz/question_form.html', {
        'exam': exam,
        'question_form': question_form,
        'formset': formset,
    })

def exam_delete(request, exam_id):
    """Vista para eliminar un examen"""
    exam = get_object_or_404(Exam, id=exam_id)
    if request.method == 'POST':
        exam.delete()
        messages.success(request, 'Examen eliminado correctamente.')
        return redirect('exam_list')
    return render(request, 'quiz/exam_confirm_delete.html', {'exam': exam})


def question_delete(request, exam_id, question_id):
    """Vista para eliminar una pregunta de un examen"""
    exam = get_object_or_404(Exam, id=exam_id)
    question = get_object_or_404(Question, id=question_id)
    
    # Verificar si la pregunta pertenece al examen
    if question.exam != exam:
        messages.error(request, "Esta pregunta no pertenece a este examen.")
        return redirect('exam_detail', exam_id=exam.id)
    
    # Eliminar la pregunta
    question.delete()
    messages.success(request, 'Pregunta eliminada correctamente.')
    
    # Redirigir al detalle del examen
    return redirect('exam_detail', exam_id=exam.id)


def quiz_play(request, exam_id):
    """Vista para jugar el quiz"""
    exam = get_object_or_404(Exam, id=exam_id)
    questions = exam.questions.all()
    
    # Revisar si el usuario ha enviado las respuestas
    if request.method == 'POST':
        score = 0
        total_questions = len(questions)
        
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')
            correct_choice = question.choices.filter(is_correct=True).first()
            if user_answer == str(correct_choice.id):
                score += 1
        
        # Mostrar el puntaje
        messages.success(request, f'Has obtenido {score} de {total_questions} preguntas correctas.')
        return redirect('exam_list')  # Redirigir a la lista de exámenes después de jugar
    
    return render(request, 'quiz/quiz_play.html', {'exam': exam, 'questions': questions})

