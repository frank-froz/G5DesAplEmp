# news/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import Comment 
from django.db import models



class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'author']
