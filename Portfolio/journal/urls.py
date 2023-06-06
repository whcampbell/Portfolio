from django.urls import path
from . import views

app_name='journal'
urlpatterns = [
    path('', views.index, name='index'),
    path('entry/<int:pk>', views.entry_detail, name='entry'),
]