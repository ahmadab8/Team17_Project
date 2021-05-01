from django.urls import path
from . import views

from django.contrib.auth import views as authViews

app_name = 'classroom'

urlpatterns = [
    path('signup/', views.SignUp, name="signup"), 
    path('signup/student_signup/', views.StudentSignUp, name="StudentSignUp"), 
    path('signup/teacher_signup/', views.TeacherSignUp, name="TeacherSignUp"), 
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('change_password/', views.change_password, name="change_password"),
    path('students_list/', views.students_list, name="students_list"),
    path('student/<int:pk>/class_notice', views.class_notice, name="class_notice"),
    path('teacher/write_notice', views.add_notice, name="write_notice"),
    path('teacher/<int:pk>/', views.TeacherDetailView.as_view(), name="teacher_detail"),
    path('update/teacher/<int:pk>/', views.TeacherUpdateView, name="teacher_update"),
    path('student/<int:pk>/all_msg', views.StudentAllMsgList.as_view(), name="all_msg_list"),
    path('class_file/', views.class_file, name="class_file"),
    path('upload_file/', views.upload_file, name="upload_file"),
    path('submit_file/<int:id>/', views.submit_file, name="submit_file"),
    path('massege_teach_admin/', views.massege_teach_admin, name="massege_teach_admin"),
    path('message_student_admin/', views.massage_student_admin, name="message_student_admin"),
    path('student/<int:pk>/add', views.add_student.as_view(), name="add_student"),    
    path('reset_password/', authViews.PasswordResetView.as_view(template_name= "classroom/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', authViews.PasswordResetDoneView.as_view(template_name= "classroom/password_reset_sent.html"), name="reset_password_done"),
    path('reset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(template_name= "classroom/password_reset_form.html"), name="reset_password_confirm"),
    path('reset_password_complete/', authViews.PasswordResetCompleteView.as_view(template_name= "classroom/password_reset_done.html"), name="reset_password_complete"),

]
