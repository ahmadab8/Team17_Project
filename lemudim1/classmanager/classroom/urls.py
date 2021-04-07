from django.urls import path
from classroom import views

app_name = 'classroom'

urlpatterns = [
    path('signup/', views.SignUp, name="signup"), # *
    path('signup/student_signup/', views.StudentSignUp, name="StudentSignUp"), # *
    path('signup/teacher_signup/', views.TeacherSignUp, name="TeacherSignUp"), # *

]