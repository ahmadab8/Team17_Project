''''asd'''
# pylint: disable=E0402,C0103
from django.urls import path
from django.contrib.auth import views as authViews
from . import views


app_name = 'classroom'

urlpatterns = [
    path('signup/',views.Sign_Up, name="signup"),
    path('signup/student_signup/', views.Student_Sign_Up, name="StudentSignUp"),
    path('signup/teacher_signup/', views.Teacher_Sign_Up, name="TeacherSignUp"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('change_password/', views.change_password, name="change_password"),
    path('students_list/', views.students_list1, name="students_list"),
    path('teachers_list/', views.teachers_list, name="teachers_list"),
    path('student/<int:pk>/class_notice', views.class_notice, name="class_notice"),
    path('teacher/write_notice', views.add_notice, name="write_notice"),
    path('teacher/<int:pk>/', views.Teacher_Detail_View.as_view(), name="teacher_detail"),
    path('update/teacher/<int:pk>/', views.Teacher_Update_View, name="teacher_update"),
    path('update/student/<int:pk>/', views.Student_Update_View, name="student_update"),
    path('student/<int:pk>/', views.Student_Detail_View.as_view(), name="student_detail"),
    path('student/<int:pk>/all_msg', views.Student_All_Msg_List.as_view(), name="all_msg_list"),
    path('student/<int:pk>/message', views.write_message, name="write_message"),
    path('class_file/', views.class_file, name="class_file"),
    path('upload_file/', views.upload_file, name="upload_file"),
    path('submit_file/<int:id>/', views.submit_file, name="submit_file"),
    path('massege_teach_admin/', views.massege_teach_admin, name="massege_teach_admin"),
    path('Change_Salary_Demand/', views.change_Salary_Demand, name="Change_Salary_Demand"),
    path('message_student_admin/', views.massage_student_admin, name="message_student_admin"),
    path('student/<int:pk>/add', views.add_student.as_view(), name="add_student"),
    path('reset_password/',authViews.PasswordResetView.as_view
    (template_name= "classroom/password_reset.html"), name="reset_password"),
    path('reset_password_sent/',authViews.PasswordResetDoneView.as_view
    (template_name= "classroom/password_reset_sent.html"), name="reset_password_done"),
    path('reset/<uidb64>/<token>/',authViews.PasswordResetConfirmView.as_view
    (template_name= "classroom/password_reset_form.html"), name="reset_password_confirm"),
    path('reset_password_complete/',authViews.PasswordResetCompleteView.as_view
    (template_name= "classroom/password_reset_done.html"), name="reset_password_complete"),
    path('alert/', views.users_alert_messages,name="alert"),
    path('file_list/', views.file_list, name="file_list"),
    path('submit_list/', views.submit_list, name="submit_list"),
    path('teacher/<int:pk>/messages_list', views.messages_list, name="messages_list"),
    path('update_file/<int:id>/', views.update_file, name="update_file"),
    path('file_delete/<int:id>/', views.file_delete, name="file_delete"),
    path('teacher/class_students_list',views.class_students_list, name="class_student_list"),
    path('student/<int:pk>/msg_list',views.student_msg_list, name="student_msg_list"),
    path('msg/<int:pk>/update',views.update_msg, name="update_msg"),
    path('student/<int:pk>/enter_msg', views.add_msg, name="enter_msg"),
    path('contact/',views.Contact_Us,name="contact"),




]
