from django.urls import path
from . import views

app_name = 'teams'

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('new/', views.team_create, name='team_create'),
    path('<int:pk>/', views.team_detail, name='team_detail'),
]