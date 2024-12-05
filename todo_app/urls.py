from django.urls import path
from .views import (
    TaskCreateView,
    TaskDetailView,
    TaskListView,
    TaskUpdateView,
    TaskDeleteView,
)
from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
]

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page to view tasks
    path('add/', views.add_task, name='add_task'),  # Add task page
    # Add other necessary paths for updating, deleting, etc.
]
