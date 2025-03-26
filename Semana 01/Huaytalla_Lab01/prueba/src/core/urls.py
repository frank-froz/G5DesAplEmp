from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='items_list'),
]