from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Ensure tag names are unique

    def __str__(self):
        return self.name


from django.db import models

class Task(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  # Remove `default`
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("OPEN", "OPEN"),
            ("WORKING", "WORKING"),
            ("PENDING REVIEW", "PENDING REVIEW"),
            ("COMPLETED", "COMPLETED"),
            ("OVERDUE", "OVERDUE"),
            ("CANCELLED", "CANCELLED"),
        ],
        default="OPEN",
    )
    tags = models.ManyToManyField("Tag", blank=True)


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



