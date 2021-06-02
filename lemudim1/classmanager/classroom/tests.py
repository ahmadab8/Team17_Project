'''tests'''
from django.test import TestCase,Client
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
# pylint: disable=E0602,C0116,W1309,C0103,E0402,W0401,R0904
from .views import *
from .auth import *
# Create your tests here.

class BaseTest(TestCase):
    '''base_test'''
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




class Unit_Test_url(TestCase):
    '''Unit_Test_url'''
#29 url test

    def test_massege_teach_admin_url_page_correctly(self):
        response = self.client.get('/classroom/massege_teach_admin/')
        self.assertEqual(response.status_code, 302)
    def test_Change_Salary_Demand_url_page_correctly(self):
        response = self.client.get('/classroom/Change_Salary_Demand/')
        self.assertEqual(response.status_code, 302)
    def test_student_add_url_page_correctly(self):
        response = self.client.get('/classroom/student/5/add')
        self.assertEqual(response.status_code, 302)
    def test_reset_password_sent_url_page_correctly(self):
        response = self.client.get('/classroom/reset_password_sent/')
        self.assertEqual(response.status_code, 200)
    def test_reset_password_complete_url_page_correctly(self):
        response = self.client.get('/classroom/reset_password_complete/')
        self.assertEqual(response.status_code, 200)
    def test_alert_url_page_correctly(self):
        response = self.client.get('/classroom/alert/')
        self.assertEqual(response.status_code, 200)
    def test_teacher_messages_list_url_page_correctly(self):
        response = self.client.get('/classroom/teacher/5/messages_list')
        self.assertEqual(response.status_code, 302)
    def test_update_file_url_page_correctly(self):
        response = self.client.get('/classroom/update_file/5/')
        self.assertEqual(response.status_code, 302)
    def test_file_delete_url_page_correctly(self):
        response = self.client.get('/classroom/file_delete/5/')
        self.assertEqual(response.status_code, 302)
    def test_signup_url_page_correctly(self):
        response = self.client.get('/classroom/signup/')
        self.assertEqual(response.status_code, 200)
    def test_class_students_list_url_page_correctly(self):
        response = self.client.get('/classroom/teacher/class_students_list')
        self.assertEqual(response.status_code, 302)
    def test_login_url_page_correctly(self):
        response = self.client.get('/classroom/login/')
        self.assertEqual(response.status_code, 200)
    def test_TeacherSignUp_url_page_correctly(self):
        response = self.client.get('/classroom/signup/teacher_signup/')
        self.assertEqual(response.status_code, 200)
    def test_StudentSignUp_url_page_correctly(self):
        response = self.client.get('/classroom/signup/student_signup/')
        self.assertEqual(response.status_code, 200)
    def test_HomePage_url_page_correctly(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_message_student_admin_url_page_correctly(self):
        response = self.client.get('/classroom/message_student_admin/')
        self.assertEqual(response.status_code, 302)
    def test_upload_file_url_page_correctly(self):
        response = self.client.get('/classroom/upload_file/')
        self.assertEqual(response.status_code, 302)
    def test_submit_file_url_page_correctly(self):
        response = self.client.get('/classroom/submit_file/5')
        self.assertEqual(response.status_code, 301)
    def test_class_notice_url_page_correctly(self):
        response = self.client.get('/classroom/student/5/class_notice')
        self.assertEqual(response.status_code, 302)
    def test_student_all_msg_url_page_correctly(self):
        response = self.client.get('/classroom/student/5/all_msg')
        self.assertEqual(response.status_code, 302)
    def test_teacher_write_notice_url_page_correctly(self):
        response = self.client.get('/classroom/teacher/write_notice')
        self.assertEqual(response.status_code, 302)
    def test_update_msg_url_page_correctly(self):
        response = self.client.get('/classroom/msg/5/update')
        self.assertEqual(response.status_code,302)
    def test_contact_url_page_correctly(self):
        response = self.client.get('/classroom/contact')
        self.assertEqual(response.status_code,301)
    def test_messages_list_url_page_correctly(self):
        response = self.client.get('/classroom/student/5/msg_list')
        self.assertEqual(response.status_code,302)
    def test_file_list_url_page_correctly(self):
        response = self.client.get('/classroom/file_list/')
        self.assertEqual(response.status_code,302)
    def test_submit_list_url_page_correctly(self):
        response = self.client.get('/classroom/submit_list/')
        self.assertEqual(response.status_code,302)
    def test_class_file_url_page_correctly(self):
        response = self.client.get('/classroom/class_file/')
        self.assertEqual(response.status_code,302)
    def test_student_message_url_page_correctly(self):
        response = self.client.get('/classroom/student/5/message')
        self.assertEqual(response.status_code,302)
    def test_update_student_url_page_correctly(self):
        response = self.client.get('/classroom/update/student/5/')
        self.assertEqual(response.status_code,302)

class Unit_Test_form(TestCase):
    '''Unit_Test_form'''
#6 form test
    def test_valid_Form(self):
        data={'message':'test'}
        form=MessageForm(data)
        self.assertTrue(form.is_valid())
    def test_invalid_Form(self):
        data={}
        form=UserForm(data)
        self.assertFalse(form.is_valid())
    def test_invalid1_Form(self):
        data={}
        form=StudentProfileUpdateForm(data)
        self.assertFalse(form.is_valid())
    def test_valid1_Form(self):
        data={'message':'test'}
        form=NoticeForm(data)
        self.assertTrue(form.is_valid())
    def test_invalid2_Form(self):
        data={'file_name':'a','file':'txt'}
        form=FileForm(data)
        self.assertFalse(form.is_valid())
    def test_valid2_Form(self):
        data={'name':'a','language':'txt','email':'ahmad@gmail.com',
        'phone':'0545932105','student_of':'math','student_profile_pic':'ahmed.png'}
        form=StudentProfileUpdateForm(data)
        self.assertTrue(form.is_valid())


class Unit_Test_template(BaseTest):
    '''Unit_Test_template'''
#6 template test
    def test_HomePage_view_page_correctly(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'classroom/index.html')
    def test_login_view_page_correctly(self):
        response = self.client.get('/classroom/login/')
        self.assertTemplateUsed(response, 'classroom/login.html')
    def test_signup_view_page_correctly(self):
        response = self.client.get('/classroom/signup/')
        self.assertTemplateUsed(response, 'classroom/signup.html')
    def test_TeacherSignUp_view_page_correctly(self):
        response = self.client.get('/classroom/signup/teacher_signup/')
        self.assertTemplateUsed(response, 'classroom/teacher_signup.html')
    def test_StudentSignUp_view_page_correctly(self):
        response = self.client.get('/classroom/signup/student_signup/')
        self.assertTemplateUsed(response, 'classroom/student_signup.html')
    def test_alert_view_page_correctly(self):
        response = self.client.get('/classroom/alert/')
        self.assertTemplateUsed(response, 'classroom/alert.html')


class Unit_Test_func(BaseTest):
    '''Unit_Test_func'''
#22 func view test
    def test_func_changepass(self):
        response = self.client.get(f'/classroom/change_password/')
        self.assertEqual(response.resolver_match.func,change_password)
    def test_func_write_message(self):
        response = self.client.get(f'/classroom/student/5/message')
        self.assertEqual(response.resolver_match.func,write_message)
    def test_func_class_students_list(self):
        response = self.client.get(f'/classroom/teacher/class_students_list')
        self.assertEqual(response.resolver_match.func,class_students_list)
    def test_func_update_msg(self):
        response = self.client.get(f'/classroom/msg/5/update')
        self.assertEqual(response.resolver_match.func,update_msg)
    def test_func_class_notice(self):
        response = self.client.get(f'/classroom/student/5/class_notice')
        self.assertEqual(response.resolver_match.func,class_notice)
    def test_func_add_notice(self):
        response = self.client.get(f'/classroom/teacher/write_notice')
        self.assertEqual(response.resolver_match.func,add_notice)
    def test_func_student_msg_list(self):
        response = self.client.get(f'/classroom/student/5/msg_list')
        self.assertEqual(response.resolver_match.func,student_msg_list)
    def test_func_students_list1(self):
        response = self.client.get(f'/classroom/students_list/')
        self.assertEqual(response.resolver_match.func,students_list1)
    def test_func_teachers_list(self):
        response = self.client.get(f'/classroom/teachers_list/')
        self.assertEqual(response.resolver_match.func,teachers_list)
    def test_func_class_file(self):
        response = self.client.get(f'/classroom/class_file/')
        self.assertEqual(response.resolver_match.func,class_file)
    def test_func_file_list(self):
        response = self.client.get(f'/classroom/file_list/')
        self.assertEqual(response.resolver_match.func,file_list)
    def test_func_update_file(self):
        response = self.client.get(f'/classroom/update_file/5/')
        self.assertEqual(response.resolver_match.func,update_file)
    def test_func_file_delete(self):
        response = self.client.get(f'/classroom/file_delete/5/')
        self.assertEqual(response.resolver_match.func,file_delete)
    def test_func_upload_file(self):
        response = self.client.get(f'/classroom/upload_file/')
        self.assertEqual(response.resolver_match.func,upload_file)
    def test_func_submit_file(self):
        response = self.client.get(f'/classroom/submit_file/5/')
        self.assertEqual(response.resolver_match.func,submit_file)
    def test_func_submit_list(self):
        response = self.client.get(f'/classroom/submit_list/')
        self.assertEqual(response.resolver_match.func,submit_list)
    def test_func_massege_teach_admin(self):
        response = self.client.get(f'/classroom/massege_teach_admin/')
        self.assertEqual(response.resolver_match.func,massege_teach_admin)
    def test_func_massage_student_admin(self):
        response = self.client.get(f'/classroom/message_student_admin/')
        self.assertEqual(response.resolver_match.func,massage_student_admin)
    def test_func_change_Salary_Demand(self):
        response = self.client.get(f'/classroom/Change_Salary_Demand/')
        self.assertEqual(response.resolver_match.func,change_Salary_Demand)
    def test_func_Contact_Us(self):
        response = self.client.get(f'/classroom/contact/')
        self.assertEqual(response.resolver_match.func,Contact_Us)
    def test_func_users_alert_messages(self):
        response = self.client.get(f'/classroom/alert/')
        self.assertEqual(response.resolver_match.func,users_alert_messages)
    def test_func_Student_Update_View(self):
        response = self.client.get(f'/classroom/update/student/5/')
        self.assertEqual(response.resolver_match.func,Student_Update_View)






class RegisterTest(BaseTest):
    '''RegisterTest'''
#7 reg test
    def test_cant_register_user_with_invalid_email(self):
        validate_email(self.user_invalid_email['email'])
    def test_cant_register_user_withshortpassword(self):
        validate_password(self.user_short_password['password1'])
    def test_cant_register_user_unmatchingpassword(self):
        self.assertEqual(self.user_unmatching_password['password1']
                         ,self.user_unmatching_password['password2'])
    def test_student_register(self):
        a=auth()
        s=User.objects.create(username='username',password='password123',is_student=True)
        a.student_register(s)
        pregusterd=User.objects.filter(username='username').first()
        s.delete()
        self.assertIsNotNone(pregusterd)
    def test_teacher_register(self):
        a=auth()
        t=User.objects.create(username='username',password='password123',is_teacher=True)
        a.teacher_register(t)
        tregusterd=User.objects.filter(username='username').first()
        t.delete()
        self.assertIsNotNone(tregusterd)
    def test_delete_student(self):
        a=auth()
        s=User.objects.create(username='username',password='password123',is_student=True)
        a.student_register(s)
        a.delete_student(s)
        deleteds=User.objects.filter(username='username').first()
        self.assertIsNone(deleteds)
    def test_delete_teacher(self):
        a=auth()
        t=User.objects.create(username='username',password='password123',is_teacher=True)
        a.teacher_register(t)
        a.delete_teacher(t)
        deleteds=User.objects.filter(username='username').first()
        self.assertIsNone(deleteds)



class integrationtest(TestCase):
    '''integrationtest'''
#5 integration test
    def test_login_techer_add_notice_changepass(self):

        c=Client()

        response = c.get(f'/classroom/change_password/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.resolver_match.func,change_password)

        response1 = c.get(f'/classroom/teacher/write_notice')
        self.assertEqual(response1.status_code, 302)
        self.assertEqual(response1.resolver_match.func,add_notice)

    def test_login_Student_changepass_massage_student_admin(self):

        c=Client()

        response = c.get(f'/classroom/change_password/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.resolver_match.func,change_password)

        response1 = c.get(f'/classroom/message_student_admin/')
        self.assertEqual(response1.status_code, 302)
        self.assertEqual(response1.resolver_match.func,massage_student_admin)


    def test_login_Student_submit_file_class_file(self):

        c=Client()

        response = c.get(f'/classroom/class_file/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.resolver_match.func,class_file)

        response1 = c.get(f'/classroom/submit_file/5/')
        self.assertEqual(response1.status_code, 302)
        self.assertEqual(response1.resolver_match.func,submit_file)

    def test_upload_file_update_file_delete_file(self):
        c=Client()

        response = c.get(f'/classroom/upload_file/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.resolver_match.func,upload_file)

        response = c.get(f'/classroom/update_file/5/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.resolver_match.func,update_file)

        response1 = c.get(f'/classroom/file_delete/5/')
        self.assertEqual(response1.status_code, 302)
        self.assertEqual(response1.resolver_match.func,file_delete)


    def test_student_class_class_notice_change_Salary_Demand(self):

        c=Client()
        response = c.get(f'/classroom/teacher/class_students_list')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.resolver_match.func,class_students_list)

        response = c.get(f'/classroom/Change_Salary_Demand/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.resolver_match.func,change_Salary_Demand)

        response1 = c.get(f'/classroom/student/5/class_notice')
        self.assertEqual(response1.status_code, 302)
        self.assertEqual(response1.resolver_match.func,class_notice)
