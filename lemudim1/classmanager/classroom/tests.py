
from django.test import TestCase,SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_home_url_name(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
    def test_home_Template_name(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'index.html')
    def test_signup_status_code(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)
    def test_signup_url_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
    def test_signup_Template_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'signup.html')
    def test_Studentpage_status_code(self):
        response = self.client.get('/StudentSignUp/')
        self.assertEqual(response.status_code, 200)
    def test_Studentpage_url_name(self):
        response = self.client.get(reverse('StudentSignUp'))
        self.assertEqual(response.status_code, 200)
    def test_Studentpage_Template_name(self):
        response = self.client.get(reverse('StudentSignUp'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'StudentSignUp.html')