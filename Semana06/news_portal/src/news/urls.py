from django.urls import path, include
from . import views
<<<<<<< HEAD
from django.contrib.auth import views as auth_views


=======
from .views import (
    ArticleListView, 
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView
)
>>>>>>> c13109aa28db57fdab7fc52dd1fd517d12c5b10e
app_name = "news"

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="home"),
    path('comments/post/', views.post_comment, name='post_comment'),
    path("article/<slug:slug>/", views.ArticleDetailView.as_view(), name="article_detail"),
<<<<<<< HEAD
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
=======
    path("article/new/", ArticleCreateView.as_view(), name="article_create"),
    path("article/<slug:slug>/edit/", ArticleUpdateView.as_view(), name="article_update"),
>>>>>>> c13109aa28db57fdab7fc52dd1fd517d12c5b10e
]