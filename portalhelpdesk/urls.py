from os import path
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('vypis/', views.ProblemyListView.as_view(), name='vypis')
]