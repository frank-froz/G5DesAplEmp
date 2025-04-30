from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'article', 'created_at', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ('user__username', 'content')
