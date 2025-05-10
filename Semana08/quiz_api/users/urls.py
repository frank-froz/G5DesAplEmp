from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfileViewSet, QuizAttemptViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'quizattempts', QuizAttemptViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
