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
