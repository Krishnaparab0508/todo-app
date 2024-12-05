from django.test import TestCase
from todo_app.models import Task
from datetime import date, timedelta

class TaskModelTest(TestCase):
    def test_due_date_validation(self):
        task = Task(
            title="Test Task",
            description="Test Description",
            timestamp=date.today(),
            due_date=date.today() - timedelta(days=1),  # Invalid due date
        )
        with self.assertRaises(ValidationError):
            task.full_clean()  # This will raise a validation error

    def test_task_creation(self):
        task = Task.objects.create(
            title="Valid Task",
            description="Valid Description",
            due_date=date.today() + timedelta(days=1),  # Valid due date
        )
        self.assertEqual(task.title, "Valid Task")
        self.assertEqual(task.status, "OPEN")
        self.assertIsNotNone(task.timestamp)
