'''forms page'''
# pylint: disable=R0903,E0402,C0305
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Teacher, Student,ClassNotice,SubmitFile,\
    ClassFile,MessageToTeacher,StudentMsg


class UserForm(UserCreationForm):
    '''UserForm'''
    class Meta():
        '''Meta'''
        model = User
        fields = ['username', 'password1', 'password2','email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'answer'}),
            'password1': forms.PasswordInput(attrs={'class': 'answer'}),
            'password2': forms.PasswordInput(attrs={'class': 'answer'}),
            'email': forms.PasswordInput(attrs={'class': 'answer'}),
        }


class TeacherProfileForm(forms.ModelForm):
    '''TeacherProfileForm'''

    class Meta():
        '''Meta'''
        model = Teacher
        fields = ['name', 'subject_name', 'phone', 'email', 'money_per_hour',
                  'description', 'payment_way',
                  'schedule']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'answer'}),
            'subject_name': forms.TextInput(attrs={'class': 'answer'}),
            'phone': forms.NumberInput(attrs={'class': 'answer'}),
            'money_per_hour': forms.NumberInput(attrs={'class': 'answer'}),
            'description': forms.TextInput(attrs={'class': 'answer'}),
            'email': forms.EmailInput(attrs={'class': 'answer'}),
            'payment_way': forms.TextInput(attrs={'class': 'answer'}),
            'schedule': forms.TextInput(attrs={'class': 'answer'}),

        }


class TeacherProfileUpdateForm(forms.ModelForm):
    '''TeacherProfileUpdateForm'''
    class Meta():
        '''Meta'''
        model = Teacher
        fields = ['name', 'subject_name', 'email', 'phone', 'teacher_profile_pic', 'money_per_hour']


class StudentProfileForm(forms.ModelForm):
    '''StudentProfileForm'''
    class Meta():
        '''Meta'''
        model = Student
        fields = ['name', 'language', 'phone', 'email', 'student_of']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'answer'}),
            'language': forms.TextInput(attrs={'class': 'answer'}),
            'phone': forms.NumberInput(attrs={'class': 'answer'}),
            'email': forms.EmailInput(attrs={'class': 'answer'}),
            'student_of': forms.TextInput(attrs={'class': 'answer'}),
        }


class StudentProfileUpdateForm(forms.ModelForm):
    '''StudentProfileUpdateForm'''
    class Meta():
        '''Meta'''
        model = Student
        fields = ['name', 'language', 'email', 'phone', 'student_of', 'student_profile_pic']


class MessageForm(forms.ModelForm):
    '''MessageForm'''
    class Meta():
        '''Meta'''
        model = MessageToTeacher
        fields = ['message']


class MsgForm(forms.ModelForm):
    '''Mesaage Form'''
    class Meta():
        '''message form meta'''
        model = StudentMsg
        fields = ['subject_name', 'msg_obtained']


class NoticeForm(forms.ModelForm):
    '''NoticeForm'''
    class Meta():
        '''Meta'''
        model = ClassNotice
        fields = ['message']



class FileForm(forms.ModelForm):
    '''FileForm'''
    class Meta():
        '''Meta'''
        model = ClassFile
        fields = ['file_name', 'file']


class SubmitForm(forms.ModelForm):
    '''SubmitForm'''
    class Meta():
        '''Meta'''
        model = SubmitFile
        fields = ['submit']

