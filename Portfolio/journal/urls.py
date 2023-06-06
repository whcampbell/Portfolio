from django.urls import path
from . import views

app_name='journal'
urlpatterns = [
    path('', views.index, name='index'),
    path('entry-list', views.EntryList.as_view(), name='entry-list'),
    path('entry/<int:pk>', views.EntryDetail.as_view(), name='entry'),
]