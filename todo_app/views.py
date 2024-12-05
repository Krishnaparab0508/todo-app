from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer


# Create a task
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Retrieve a single task
class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Retrieve all tasks
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Update a task
class TaskUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Delete a task
class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

from django.shortcuts import render
from .models import Task

def home_view(request):
    # Retrieve all tasks from the database
    tasks = Task.objects.all()

    # Render the home page with tasks
    return render(request, 'todo_app/home.html', {'tasks': tasks})

from django.shortcuts import render, redirect
from .models import Task
from django.http import HttpResponse

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        Task.objects.create(title=title, description=description, due_date=due_date, completed=False)
        return redirect('home')

    return render(request, 'todo_app/add_task.html')

from django.shortcuts import get_object_or_404, redirect
from .models import Task

# View to mark a task as completed
def complete_task(request, task_id):
    # Get the task by ID, or return a 404 if not found
    task = get_object_or_404(Task, id=task_id)
    
    # Mark the task as completed
    task.completed = True
    task.save()

    # Redirect to the home page or task list
    return redirect('home')

from django.shortcuts import get_object_or_404, redirect
from .models import Task

# View to delete a task
def delete_task(request, task_id):
    # Get the task by ID or return a 404 if not found
    task = get_object_or_404(Task, id=task_id)

    # Delete the task from the database
    task.delete()

    # Redirect to the home page or task list
    return redirect('home')
