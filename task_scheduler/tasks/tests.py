from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Tasks


class TasksViewsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.task = Tasks.objects.create(user=self.user, task_name='Test Task', date_deadline='2023-10-23 00:00:00')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/home.html')

    def test_task_update_view(self):
        response = self.client.get(reverse('update', args=[str(self.task.pk)]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_update.html')

    def test_export_csv_view(self):
        response = self.client.get(reverse('export-csv'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('Content-Type'), 'text/csv')

