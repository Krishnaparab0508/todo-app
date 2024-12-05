from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField(default='2024-12-31')
    completed = models.BooleanField(default=False)
  # Default to False
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
from django.shortcuts import render, redirect
from .models import Task

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        # Only pass the required fields and let 'completed' default to False
        Task.objects.create(
            title=title, 
            description=description, 
            due_date=due_date
        )
        return redirect('home')

    return render(request, 'todo_app/add_task.html')



