from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    bio = models.TextField(blank=True)
    dark_mode = models.BooleanField(default=False)
    bookmarks = models.ManyToManyField('news.Article', blank=True, related_name='bookmarked_by')

    def __str__(self):
        return f'Perfil de {self.user.username}'
