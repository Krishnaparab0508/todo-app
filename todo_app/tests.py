import django
django.setup()

from django.test import TestCase
from .models import Task

class TaskTest(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(
            title="Test Task",
            description="This is a test task.",
            due_date="2024-12-10",
            status="OPEN",
        )
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.status, "OPEN")
from django.test import TestCase
from .models import Task, Tag

class TaskModelTest(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            due_date="2024-12-10"
        )
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")

