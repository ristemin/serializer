from django import views
from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.home, name="home"),
    path('task-list/', views.taskList, name='task-list'),
    path('task-list/<str:pk>/', views.taskDetail, name='task-detail'),
    path('task-update/<str:pk>/', views.taskUpdate, name='task-update'),
    path('task-delete/<str:pk>/', views.taskDelete, name='task-delete'),
    path('task-create', views.taskCreate, name="task-create"),

]