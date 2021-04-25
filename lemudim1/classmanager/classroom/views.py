from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render
from . models import  message_teach_admin
from . models import  message_student_admin

from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
from django.views.generic import  (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView)
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm,TeacherProfileForm,FileForm,SubmitForm,StudentProfileForm,TeacherProfileUpdateForm,StudentProfileUpdateForm,NoticeForm
from django.urls import reverse
from classroom import models
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from .models import Student,Teacher,ClassNotice,StudentsInClass,StudentMsg,SubmitFile,ClassFile

# Create your views here.



def TeacherSignUp(request): 
    user_type = 'teacher'
    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        teacher_profile_form = TeacherProfileForm(data = request.POST)

        if user_form.is_valid() and teacher_profile_form.is_valid():

            user = user_form.save()
            user.is_teacher = True
            user.save()

            profile = teacher_profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors,teacher_profile_form.errors)
    else:
        user_form = UserForm()
        teacher_profile_form = TeacherProfileForm()

    return render(request,'classroom/teacher_signup.html',{'user_form':user_form,'teacher_profile_form':teacher_profile_form,'registered':registered,'user_type':user_type})


def StudentSignUp(request): # *
    user_type = 'student'
    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        student_profile_form = StudentProfileForm(data = request.POST)

        if user_form.is_valid() and student_profile_form.is_valid():

            user = user_form.save()
            user.is_student = True
            user.save()

            profile = student_profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors,student_profile_form.errors)
    else:
        user_form = UserForm()
        student_profile_form = StudentProfileForm()

    return render(request,'classroom/student_signup.html',{'user_form':user_form,'student_profile_form':student_profile_form,'registered':registered,'user_type':user_type})

def SignUp(request): 
    return render(request,'classroom/signup.html',{})


## login view.
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse("Account not active")

        else:
            messages.error(request, "Invalid Details")
            return redirect('classroom:login')
    else:
        return render(request,'classroom/login.html',{})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST , user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password changed")
            return redirect('home')
        else:
            return redirect('classroom:change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request,'classroom/change_password.html',args)



@login_required
def class_notice(request,pk):
    student = get_object_or_404(models.Student,pk=pk)
    return render(request,'classroom/class_notice_list.html',{'student':student})



@login_required
def add_notice(request):
    notice_sent = False
    teacher = request.user.Teacher
    students = StudentsInClass.objects.filter(teacher=teacher)
    students_list = [x.student for x in students]

    if request.method == "POST":
        notice = NoticeForm(request.POST)
        if notice.is_valid():
            object = notice.save(commit=False)
            object.teacher = teacher
            object.save()
            object.students.add(*students_list)
            notice_sent = True
    else:
        notice = NoticeForm()
    return render(request,'classroom/write_notice.html',{'notice':notice,'notice_sent':notice_sent})




def students_list(request):
    query = request.GET.get("q", None)
    students = StudentsInClass.objects.filter(teacher=request.user.Teacher)
    students_list = [x.student for x in students]
    qs = Student.objects.all()
    if query is not None:
        qs = qs.filter(
                Q(name__icontains=query)
                )
    qs_one = []
    for x in qs:
        if x in students_list:
            pass
        else:
            qs_one.append(x)

    context = {
        "students_list": qs_one,
    }
    template = "classroom/students_list.html"
    return render(request, template, context)


class StudentAllMsgList(LoginRequiredMixin, DetailView):
    model = models.Student
    template_name = "classroom/student_allmsg_list.html"
    context_object_name = "student"
    
@login_required
def student_msg_list(request, pk):
    error = True
    student = get_object_or_404(models.Student,pk=pk)
    teacher = request.user.Teacher
    given_msg = StudentMsg.objects.filter(teacher=teacher,student=student)
    return render(request,'classroom/student_msg_list.html',{'student':student,'given_msg':given_msg})


@login_required
def class_file(request):
    student = request.user.Student
    file = SubmitFile.objects.filter(student=student)
    file_list = [x.submitted_file for x in file]
    return render(request,'classroom/class_file.html',{'student':student,'file_list':file_list})

@login_required
def upload_file(request):
    file_uploaded = False
    teacher = request.user.Teacher
    students = Student.objects.filter(user_student_name__teacher=request.user.Teacher)
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.teacher = teacher
            students = Student.objects.filter(user_student_name__teacher=request.user.Teacher)
            upload.save()
            upload.student.add(*students)
            file_uploaded = True
    else:
        form = FileForm()
    return render(request,'classroom/upload_file.html',{'form':form,'file_uploaded':file_uploaded})

@login_required
def submit_file(request, id=None):
    student = request.user.Student
    file = get_object_or_404(ClassFile, id=id)
    teacher = file.teacher
    if request.method == 'POST':
        form = SubmitForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.teacher = teacher
            upload.student = student
            upload.submitted_file = file
            upload.save()
            return redirect('classroom:class_file')
    else:
        form = SubmitForm()
    return render(request,'classroom/submit_file.html',{'form':form,})
@login_required
def massege_teach_admin(request):
    if request.method == 'POST':
        message1 = request.POST['message1']
        print(message1)
        obj = message_teach_admin()
        obj.message=message1
        obj.save()

    context={}

    return render(request,'classroom/massege_teach_admin.html',{})

@login_required
def massage_student_admin(request):
    if request.method == 'POST':
        message2 = request.POST['message2']
        print(message2)
        obj2 = message_student_admin()
        obj2.message=message2
        obj2.save()

    context={}

    return render(request,'classroom/message_student_admin.html',{})