from django.test import TestCase, Client
from django.urls import reverse
from .models import Task

class TaskTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(title="Test Task")

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_task_create_view(self):
        response = self.client.post(reverse('task_create'), {
            'title': 'New Task',
            'description': 'Description',
            'completed': False
        })
        self.assertEqual(response.status_code, 302) # Redirects after success
        self.assertEqual(Task.objects.count(), 2)

    def test_task_update_view(self):
        response = self.client.post(reverse('task_update', args=[self.task.pk]), {
            'title': 'Updated Task',
            'description': '',
            'completed': True
        })
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')
        self.assertTrue(self.task.completed)

    def test_task_delete_view(self):
        response = self.client.post(reverse('task_delete', args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)

    def test_task_toggle_complete(self):
        self.assertFalse(self.task.completed)
        self.client.get(reverse('task_toggle_complete', args=[self.task.pk]))
        self.task.refresh_from_db()
        self.assertTrue(self.task.completed)
