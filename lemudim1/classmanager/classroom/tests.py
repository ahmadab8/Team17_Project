from django.test import TestCase,Client
from django.core.validators import validate_email
from django.contrib.auth import authenticate
from .models import *
from django.contrib.auth.password_validation import validate_password
from .views import *
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
                'password1': 'tes121qweqwe',
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

    def test_message_student_admin_view_page_correctly(self):
        response = self.client.get('/classroom/message_student_admin/')
        self.assertEqual(response.status_code, 302)
    
    def test_upload_file_view_page_correctly(self):
        response = self.client.get('/classroom/upload_file/')
        self.assertEqual(response.status_code, 302)
    
    def test_submit_file_view_page_correctly(self):
        response = self.client.get('/classroom/submit_file/5')
        self.assertEqual(response.status_code, 301)
    
    def test_class_notice_view_page_correctly(self):
        response = self.client.get('/classroom/student/5/class_notice')
        self.assertEqual(response.status_code, 302)
    
    def test_student_all_msg_view_page_correctly(self):
        response = self.client.get('/classroom/student/5/all_msg')
        self.assertEqual(response.status_code, 302)
    
    def test_teacher_write_notice_view_page_correctly(self):
        response = self.client.get('/classroom/teacher/write_notice')
        self.assertEqual(response.status_code, 302)
    
    

class RegisterTest(BaseTest):

    def test_cant_register_user_with_invalid_email(self):
       validate_email(self.user_invalid_email['email'])
    
    def test_cant_register_user_withshortpassword(self):
        validate_password(self.user_short_password['password1'])

    def test_cant_register_user_unmatchingpassword(self):
        self.assertEqual(self.user_unmatching_password['password1'],self.user_unmatching_password['password2'])

    
    

class integrationtest(TestCase):

    def test_login_techer_add_notice_changepass(self):

        t=User.objects.create(password='12345aaaaa@',username='username',is_teacher=True)
        t.save()
        c=Client()
        c.login(password=t.password,username=t.username)

        response = c.get(f'/classroom/change_password/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.resolver_match.func,change_password)

        response1 = c.get(f'/classroom/teacher/write_notice')
        self.assertEqual(response1.status_code, 302)
        self.assertEqual(response1.resolver_match.func,add_notice)

    def test_login_Student_changepass_massage_student_admin(self):

        t=User.objects.create(password='12345aaaaa@',username='username',is_student=True)
        t.save()
        c=Client()
        c.login(password=t.password,username=t.username)

        response = c.get(f'/classroom/change_password/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.resolver_match.func,change_password)

        response1 = c.get(f'/classroom/message_student_admin/')
        self.assertEqual(response1.status_code, 302)
        self.assertEqual(response1.resolver_match.func,massage_student_admin)
      

    def test_login_Student_submit_file_class_file(self):

        t=User.objects.create(password='12345aaaaa@',username='username',is_student=True)
        t.save()
        c=Client()
        c.login(password=t.password,username=t.username)

        response = c.get(f'/classroom/class_file/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.resolver_match.func,class_file)

        response1 = c.get(f'/classroom/submit_file/5/')
        self.assertEqual(response1.status_code, 302)
        self.assertEqual(response1.resolver_match.func,submit_file)
      