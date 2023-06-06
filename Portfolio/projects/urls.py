from django.urls import path
from . import views

app_name='projects'
urlpatterns = [
    path('', views.index, name='index'),
    path('snake/', views.snake, name='snake'),
]