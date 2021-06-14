from django.test import TestCase
from django.urls import reverse
from .views import SnackDetailView, SnackListView

# Create your tests here.

class snackTests(TestCase):
    def test_home_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_about_page_status_code(self):
        url = reverse('snack_detail', args="1")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_about_page_template(self):
        url = reverse('snack_detail', args="1")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)