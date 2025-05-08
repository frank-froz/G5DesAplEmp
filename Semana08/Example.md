# Building a Quiz API with Django REST Framework 🧠📝

A step-by-step guide to creating a Quiz API using Django REST Framework, focusing on model relationships, serialization, and REST principles.

## Table of Contents

- [Building a Quiz API with Django REST Framework 🧠📝](#building-a-quiz-api-with-django-rest-framework-)
  - [Table of Contents](#table-of-contents)
  - [1. Understanding the Concept](#1-understanding-the-concept)
    - [What We're Building](#what-were-building)
    - [Main Components](#main-components)
    - [API Endpoints Overview](#api-endpoints-overview)
    - [Data Flow](#data-flow)
  - [2. Environment Setup](#2-environment-setup)
    - [Creating Project Directory](#creating-project-directory)
    - [Setting Up Virtual Environment](#setting-up-virtual-environment)
    - [Installing Dependencies](#installing-dependencies)
    - [Project Configuration](#project-configuration)
  - [3. Implementation](#3-implementation)
    - [Step 1: Creating Models](#step-1-creating-models)
    - [Step 2: Setting Up Serializers](#step-2-setting-up-serializers)
    - [Step 3: Building Views](#step-3-building-views)
    - [Step 4: Configuring URLs](#step-4-configuring-urls)
    - [Step 5: Adding Validation Endpoint](#step-5-adding-validation-endpoint)
    - [Step 6: Testing the API](#step-6-testing-the-api)
  - [4. Testing and Verification](#4-testing-and-verification)
    - [Manual Testing with the Django REST Framework UI](#manual-testing-with-the-django-rest-framework-ui)
    - [Testing with API Requests](#testing-with-api-requests)
    - [Validating Quiz Answers](#validating-quiz-answers)
  - [5. Next Steps](#5-next-steps)
    - [Additional Applications](#additional-applications)
    - [Feature Enhancements](#feature-enhancements)
    - [Learning Challenges](#learning-challenges)

## 1. Understanding the Concept

### What We're Building

We'll create a Quiz API that allows users to:
- Create, read, update, and delete quizzes
- Add questions with multiple choices to quizzes
- Submit answers and receive validation

This project focuses on learning how to implement relationships between models in Django REST Framework (DRF) and how to properly serialize nested data structures.

### Main Components

Our API will consist of these key components:

```
Quiz API
├── Models
│   ├── Quiz (title, description, etc.)
│   ├── Question (belongs to a quiz, contains text)
│   └── Choice (belongs to a question, has text and correctness flag)
├── Serializers
│   ├── Basic serializers for individual models
│   └── Nested serializers for related data
├── Views
│   ├── ViewSets for CRUD operations
│   └── Custom view for answer validation
└── URLs for routing requests
```

### API Endpoints Overview

We'll implement these endpoints:

- `/api/quizzes/` - List all quizzes and create new ones
- `/api/quizzes/<id>/` - Retrieve, update, or delete a specific quiz
- `/api/questions/` - List all questions and create new ones
- `/api/questions/<id>/` - Retrieve, update, or delete a specific question
- `/api/choices/` - List all choices and create new ones 
- `/api/choices/<id>/` - Retrieve, update, or delete a specific choice
- `/api/quizzes/<id>/validate/` - Validate submitted answers for a quiz

### Data Flow

Here's how data flows through our application:

```
Request → URL Router → View → Serializer → Model → Database
                                ↑
Response ← Serializer ← Model ←┘
```

When a client submits answers:

```
POST /api/quizzes/1/validate/
{
  "answers": [
    {"question_id": 1, "choice_id": 2},
    {"question_id": 2, "choice_id": 5}
  ]
}

→ Validation View processes the answers
→ Checks if choices are correct
→ Returns results to the client
```

## 2. Environment Setup

### Creating Project Directory

First, let's create our project directory:

```bash
# Create project directory
mkdir quiz_api
cd quiz_api
```

### Setting Up Virtual Environment

Create and activate a virtual environment:

```bash
# Create virtual environment
python3 -m venv venv

# Activate on Windows
# venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### Installing Dependencies

Install Django, Django REST Framework, and other dependencies:

```bash
# Install dependencies
pip install django djangorestframework
pip freeze > requirements.txt
```

### Project Configuration

Create a Django project and app:

```bash
# Create Django project
django-admin startproject config .

# Create a dedicated app for our quiz functionality
python manage.py startapp quizzes
```

Update `config/settings.py` to include our app and DRF:

```python
INSTALLED_APPS = [
    # Django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',
    
    # Local apps
    'quizzes',
]

# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # For development - change in production
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

## 3. Implementation

### Step 1: Creating Models

First, let's define our models in `quizzes/models.py`:

```python
from django.db import models


class Quiz(models.Model):
    """Model for quizzes"""
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "quizzes"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class Question(models.Model):
    """Model for questions within a quiz"""
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.text


class Choice(models.Model):
    """Model for answer choices for a question"""
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.text
```

Create and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Register models in `quizzes/admin.py`:

```python
from django.contrib import admin
from .models import Quiz, Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 3


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'quiz']
    list_filter = ['quiz']
    search_fields = ['text']
    inlines = [ChoiceInline]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['text', 'question', 'is_correct']
    list_filter = ['question', 'is_correct']
    search_fields = ['text']
```

### Step 2: Setting Up Serializers

Next, let's create serializers in a new file `quizzes/serializers.py`:

```python
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
```

### Step 3: Building Views

Now, let's create our views in `quizzes/views.py`:

```python
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
```

### Step 4: Configuring URLs

Now, let's configure our URLs. First, create `quizzes/urls.py`:

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, QuestionViewSet, ChoiceViewSet

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

Then, update `config/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('quizzes.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
```

### Step 5: Adding Validation Endpoint

We've already implemented the validation endpoint in our `QuizViewSet` using the `@action` decorator. This allows us to handle POST requests to `/api/quizzes/<id>/validate/`.

### Step 6: Testing the API

Create a superuser to access the admin site:

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

## 4. Testing and Verification

### Manual Testing with the Django REST Framework UI

You can test your API using the browsable API provided by Django REST Framework:

1. Go to `http://127.0.0.1:8000/api/quizzes/` to see all quizzes.
2. Create a new quiz by filling out the form.
3. To add questions, go to `http://127.0.0.1:8000/api/questions/` and create a question linked to your quiz.
4. To add choices, go to `http://127.0.0.1:8000/api/choices/` and create choices for your question.

### Testing with API Requests

You can also use tools like cURL, Postman, or HTTPie to test your API. Here are some examples:

**Creating a quiz:**

```bash
curl -X POST http://127.0.0.1:8000/api/quizzes/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Python Basics", "description": "Test your knowledge of Python fundamentals"}'
```

**Creating a question:**

```bash
curl -X POST http://127.0.0.1:8000/api/questions/ \
  -H "Content-Type: application/json" \
  -d '{"quiz": 1, "text": "What is the output of print(1 + 2)?"}'
```

**Creating choices:**

```bash
curl -X POST http://127.0.0.1:8000/api/choices/ \
  -H "Content-Type: application/json" \
  -d '{"question": 1, "text": "3", "is_correct": true}'

curl -X POST http://127.0.0.1:8000/api/choices/ \
  -H "Content-Type: application/json" \
  -d '{"question": 1, "text": "12", "is_correct": false}'
```

### Validating Quiz Answers

Testing the validation endpoint:

```bash
curl -X POST http://127.0.0.1:8000/api/quizzes/1/validate/ \
  -H "Content-Type: application/json" \
  -d '{"answers": [{"question_id": 1, "choice_id": 1}]}'
```

Expected response:

```json
{
  "quiz_id": 1,
  "score": "1/1",
  "percentage": 100,
  "results": [
    {
      "question_id": 1,
      "correct": true,
      "correct_choice": null
    }
  ]
}
```

## 5. Next Steps

### Additional Applications

Here are three applications you could develop to extend your Quiz API:

1. **User Management System** 👥

   Create an app to handle user authentication and profiles:
   
   ```python
   # users/models.py
   from django.db import models
   from django.contrib.auth.models import User
   
   class Profile(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE)
       bio = models.TextField(blank=True)
       avatar = models.ImageField(upload_to='avatars/', blank=True)
       created_at = models.DateTimeField(auto_now_add=True)
       
       def __str__(self):
           return f"{self.user.username}'s profile"
   
   class QuizAttempt(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attempts')
       quiz = models.ForeignKey('quizzes.Quiz', on_delete=models.CASCADE)
       score = models.IntegerField()
       max_score = models.IntegerField()
       completed_at = models.DateTimeField(auto_now_add=True)
       
       def __str__(self):
           return f"{self.user.username} - {self.quiz.title}: {self.score}/{self.max_score}"
   ```

2. **Quiz Categories and Tags** 🏷️

   Create an app to organize quizzes with categories and tags:
   
   ```python
   # categories/models.py
   from django.db import models
   
   class Category(models.Model):
       name = models.CharField(max_length=100)
       description = models.TextField(blank=True)
       
       class Meta:
           verbose_name_plural = "categories"
       
       def __str__(self):
           return self.name
   
   class Tag(models.Model):
       name = models.CharField(max_length=50)
       
       def __str__(self):
           return self.name
   
   # Then add to quizzes/models.py:
   # category = models.ForeignKey('categories.Category', on_delete=models.SET_NULL, null=True, related_name='quizzes')
   # tags = models.ManyToManyField('categories.Tag', related_name='quizzes', blank=True)
   ```

3. **Quiz Analytics System** 📊

   Create an app to track and analyze quiz performance:
   
   ```python
   # analytics/models.py
   from django.db import models
   from django.contrib.auth.models import User
   
   class QuestionStat(models.Model):
       question = models.ForeignKey('quizzes.Question', on_delete=models.CASCADE, related_name='stats')
       attempts = models.IntegerField(default=0)
       correct_attempts = models.IntegerField(default=0)
       
       @property
       def success_rate(self):
           return (self.correct_attempts / self.attempts) * 100 if self.attempts > 0 else 0
       
       def __str__(self):
           return f"Stats for: {self.question.text[:30]}..."
   
   class QuizActivity(models.Model):
       quiz = models.ForeignKey('quizzes.Quiz', on_delete=models.CASCADE, related_name='activities')
       date = models.DateField(auto_now_add=True)
       views = models.IntegerField(default=0)
       starts = models.IntegerField(default=0)
       completions = models.IntegerField(default=0)
       
       class Meta:
           unique_together = ['quiz', 'date']
       
       def __str__(self):
           return f"{self.quiz.title} activity on {self.date}"
   ```

### Feature Enhancements

Consider implementing these features to enhance your Quiz API:

1. **Timed Quizzes** ⏱️
   - Add a time limit to quizzes
   - Track time taken by users
   - Auto-submit when time expires

2. **Question Types** 📋
   - Multiple-choice (select one)
   - Multiple-select (select many)
   - True/False questions
   - Short answer questions

3. **Access Control** 🔒
   - Public vs. private quizzes
   - Password-protected quizzes
   - Quiz invitations via email

4. **Media Support** 🖼️
   - Images in questions
   - Audio or video questions
   - File upload answers

5. **Feedback System** 💬
   - Immediate feedback after each question
   - Detailed explanations for correct answers
   - Personalized improvement suggestions

### Learning Challenges

Here are five challenges to help you deepen your understanding of Django REST Framework:

1. Implement JWT authentication for the API
2. Add permission classes to limit who can create/edit quizzes
3. Create a custom filter to search quizzes by difficulty level
4. Add API throttling to prevent abuse
5. Implement API versioning to support multiple versions

By completing this project, you've learned how to create a fully functional Quiz API with Django REST Framework, implementing model relationships, serialization, and custom endpoints. The additional applications and enhancements will help you expand your skills further as you continue to develop your API.