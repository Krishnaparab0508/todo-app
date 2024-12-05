from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[('OPEN', 'Open'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed')],
        default='OPEN'  # Set a default value for the status field
    )
    
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



