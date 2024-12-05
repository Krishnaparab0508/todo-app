from rest_framework.test import APIClient
from django.test import TestCase
from todo_app.models import Task
from rest_framework import status

class TaskAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            due_date="2024-12-31"
        )

    def test_create_task(self):
        response = self.client.post('/api/tasks/', {
            'title': 'New Task',
            'description': 'New Description',
            'due_date': '2024-12-31',
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_task(self):
        response = self.client.get(f'/api/tasks/{self.task.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task.title)

    def test_update_task(self):
        response = self.client.put(f'/api/tasks/{self.task.id}/', {
            'title': 'Updated Task',
            'description': 'Updated Description',
            'due_date': '2024-12-31',
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Task')

    def test_delete_task(self):
        response = self.client.delete(f'/api/tasks/{self.task.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
