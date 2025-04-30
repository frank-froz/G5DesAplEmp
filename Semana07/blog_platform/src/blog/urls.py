from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Home page (post list)
    path('', views.PostListView.as_view(), name='post_list'),
    
    # Post detail
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    
    # Category posts
    path('category/<slug:slug>/', views.CategoryPostListView.as_view(), name='category_detail'),
    
    # Tag posts
    path('tag/<slug:slug>/', views.TagPostListView.as_view(), name='tag_detail'),
    
    # Add comment
    path('post/<slug:slug>/comment/', views.CommentCreateView.as_view(), name='add_comment'),
]