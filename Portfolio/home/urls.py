from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('about/', views.about, name='about'),
]