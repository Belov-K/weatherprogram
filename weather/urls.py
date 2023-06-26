from django.urls import path
from . import views

app_name='weather'
urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('documents/', views.documents, name='documents'),
]
