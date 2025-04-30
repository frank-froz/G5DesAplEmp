from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


app_name = "news"

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="home"),
    path('comments/post/', views.post_comment, name='post_comment'),
    path("article/<slug:slug>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]