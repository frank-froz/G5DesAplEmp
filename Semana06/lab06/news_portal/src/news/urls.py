from django.urls import path
from . import views
from .views import (
    ArticleListView, 
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView
)
app_name = "news"

urlpatterns = [
    # Home page with latest articles
    path("", views.ArticleListView.as_view(), name="home"),
    
    # Article detail page
    path("article/<slug:slug>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path("article/new/", ArticleCreateView.as_view(), name="article_create"),
    path("article/<slug:slug>/edit/", ArticleUpdateView.as_view(), name="article_update"),
]