import regex as regex
from django.core.validators import validate_email
from django.test import TestCase,SimpleTestCase
from django.urls import reverse
from .models import Teacher
from django.core import mail


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



class modelTest(TestCase):


    def setUp(self):
        self.register_url = reverse('signup')
        self.user = {
            'email': 'testemail@gmail.com',
            'username': 'username',
            'Age': '18',
            'per_hour': '50',
            'subject': 'arabic',
            'password': 'password',
            'confirm': 'password',
            'name': 'fullname'
        }

        self.user_unmatching_password = {

            'email': 'testemail@gmail.com',
            'username': 'username',
            'Age': '18',
            'per_hour': '50',
            'subject': 'arabic',
            'password': 'password',
            'confirm': 'password',
            'name': 'fullname'
        }
        self.user_invalid_email = {

            'email': 'testemail@gmail.com',
            'username': 'username',
            'Age': '18',
            'per_hour': '50',
            'subject': 'arabic',
            'password': 'password',
            'confirm': 'password',
            'name': 'fullname'
        }

        return super().setUp()


    def test_can_register_user(self):
        response = self.client.post(self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 200)


    def test_cant_register_user_with_unmatching_passwords(self):
        response = self.client.post(self.register_url, self.user_unmatching_password, format='text/html')
        self.assertEqual(self.user_unmatching_password['password'], self.user_unmatching_password['confirm'])

    def test_cant_register_user_with_invalid_email(self):
       validate_email(self.user_invalid_email['email'])



class model2Test(TestCase):


    def setUp(self):
        self.register_url = reverse('StudentSignUp')
        self.user = {
            'email': 'testemail@gmail.com',
            'username': 'username',
            'password': 'password',
            'confirm': 'password',
            'first_name': 'basel',
            'Last_name': 'mahamid'
        }

        self.user_unmatching_password = {

            'email': 'testemail@gmail.com',
            'username': 'username',
            'password': 'password',
            'confirm': 'password',
            'first_name': 'basel',
            'Last_name': 'mahamid'
        }
        self.user_invalid_email = {

            'email': 'testemail@gmail.com',
            'username': 'username',
            'password': 'password',
            'confirm': 'password',
            'first_name': 'basel',
            'Last_name': 'mahamid'
        }

        return super().setUp()


    def test_can_register_user(self):
        response = self.client.post(self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 200)


    def test_cant_register_user_with_unmatching_passwords(self):
        response = self.client.post(self.register_url, self.user_unmatching_password, format='text/html')
        self.assertEqual(self.user_unmatching_password['password'], self.user_unmatching_password['confirm'])

    def test_cant_register_user_with_invalid_email(self):
       validate_email(self.user_invalid_email['email'])

