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
    def test_create_task_with_tags(self):
        tag1 = Tag.objects.create(name="Work")
        tag2 = Tag.objects.create(name="Urgent")
        task = Task.objects.create(
            title="Test Task",
            description="Test Task Description",
            status="OPEN"
        )
        task.tags.add(tag1, tag2)

        self.assertEqual(task.tags.count(), 2)
        self.assertIn(tag1, task.tags.all())
        self.assertIn(tag2, task.tags.all())
