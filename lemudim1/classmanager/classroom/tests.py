from django.test import TestCase
from django.core.validators import validate_email

# Create your tests here.

class BaseTest(TestCase):
    def setUp(self):
        
        self.user = {
                'email': 'testemail@gmail.com',
                'username': 'username',
                'password1': 'password4756',
                'password2': 'password4756',
                
                
            }
        self.user_short_password = {
                'email': 'testemail@gmail.com',
                'username': 'username',
                'password1': 'tes',
                'password2': 'tes',
                
            }
        self.user_unmatching_password = {

                'email': 'testemail@gmail.com',
                'username': 'username',
                'password1': 'teslatto',
                'password2': 'teslatto',
                
            }

        self.user_invalid_email = {

                'email': 'test@asd.com',
                'username': 'username',
                'password1': 'teslatto',
                'password2': 'teslatto',
                
            }
        return super().setUp()


class pagesTest(TestCase):

    
    def test_signup_view_page_correctly(self):
        response = self.client.get('/classroom/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'classroom/signup.html')
    
    def test_login_view_page_correctly(self):
        response = self.client.get('/classroom/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'classroom/login.html')
    
    def test_TeacherSignUp_view_page_correctly(self):
        response = self.client.get('/classroom/signup/teacher_signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'classroom/teacher_signup.html')

    def test_StudentSignUp_view_page_correctly(self):
        response = self.client.get('/classroom/signup/student_signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'classroom/student_signup.html')
    
    def test_HomePage_view_page_correctly(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'classroom/index.html')


class RegisterTest(BaseTest):

    def test_can_register_user(self):
        response = self.client.post('/classroom/signup/', self.user, format='text/html')
        self.assertEqual(response.status_code, 200)
    

    def test_cant_register_user_with_invalid_email(self):
       validate_email(self.user_invalid_email['email'])

    def test_cant_register_user_withshortpassword(self):
        pass
