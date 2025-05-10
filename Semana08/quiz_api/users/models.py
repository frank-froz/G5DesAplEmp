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