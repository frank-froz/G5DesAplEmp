from django.contrib import admin
from .models import Profile, QuizAttempt
from django.contrib.auth.models import User


# Registrar el modelo Profile para que se vea en el admin
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'created_at']
    search_fields = ['user__username', 'bio']

# Registrar el modelo QuizAttempt para que se vea en el admin
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ['user', 'quiz', 'score', 'max_score', 'completed_at']
    list_filter = ['quiz', 'user']
    search_fields = ['user__username', 'quiz__title']

# Registrar los modelos
admin.site.register(Profile, ProfileAdmin)
admin.site.register(QuizAttempt, QuizAttemptAdmin)
