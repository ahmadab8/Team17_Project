from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('StudentSignUp/',views.StudentSignUp,name='StudentSignUp'),
    path('TeacherRegister/', views.TeacherRegister, name='TeacherRegister'),

]