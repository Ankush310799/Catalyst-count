from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Company

class CoreViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.company_data = {
            'name': 'Test Company',
            'domain': 'test.com',
            'year_founded': 2020,
            'industry': 'IT',
            'size_range': 'Medium',
            'locality': 'Test City',
            'country': 'Test Country',
            'linkedin_url': 'https://www.linkedin.com/testcompany',
            'current_employee_estimate': 50,
            'total_employee_estimate': 100
        }

    def test_upload_file_view(self):
        response = self.client.post(reverse('upload_file'), self.company_data)
        self.assertEqual(response.status_code, 200) 

        company = Company.objects.create(name='Test Company',domain='test.com',
                            year_founded=2021, industry='IT',size_range='Medium',
                            locality='Test City',country='Test Country',
                            linkedin_url='https://www.linkedin.com/testcompany',
                            current_employee_estimate=234,
                            total_employee_estimate=786
        )
        company_count = Company.objects.count()
        self.assertEqual(company_count, 1)
        
    def test_query_builder_view(self):
        response = self.client.post(reverse('query_builder'), {'keyword': 'Test'})
        self.assertEqual(response.status_code, 200)  

        results = response.context['results']
        self.assertIsNotNone(results) 

    def test_query_count_api_view(self):
        response = self.client.get(reverse('query_count'), {'name': 'Test'})
        self.assertEqual(response.status_code, 200) 

        data = response.data
        self.assertIn('count', data) 

    def test_user_list_view(self):
        response = self.client.post(reverse('user_list'), {'username': 'newuser', 'email': 'newuser@test.com'})
        self.assertEqual(response.status_code, 302)  

        user_count = User.objects.count()
        self.assertEqual(user_count, 2)

    def test_delete_user_view(self):
        new_user = User.objects.create(username='deleteuser', email='deleteuser@test.com')
        response = self.client.post(reverse('delete_user', args=[new_user.id]))
        self.assertEqual(response.status_code, 302)

        user_exists = User.objects.filter(username='deleteuser').exists()
        self.assertFalse(user_exists) 