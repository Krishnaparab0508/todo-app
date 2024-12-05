from django.urls import path
from todo_app import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page with tasks list
    path('add/', views.add_task, name='add_task'),  # Page to add a new task
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),  # Mark a task as completed
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Delete a task
]
