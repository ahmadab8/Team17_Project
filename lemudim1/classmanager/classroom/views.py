'''views'''
# pylint: disable=C0103,W0702,E0402,R0901,R1705,E0602,W0622,E1305,W0621

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
from django.views.generic import DetailView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .models import message_teach_admin, Change_Salary_Demand, alert_for_users
from . models import  message_student_admin
from . import models
from .models import Student,Teacher,StudentsInClass,StudentMsg,SubmitFile,ClassFile,Contact
from .forms import UserForm,TeacherProfileForm,FileForm,SubmitForm,StudentProfileForm,\
TeacherProfileUpdateForm,StudentProfileUpdateForm,NoticeForm,MessageForm,MsgForm



# Create your views here.



def Teacher_Sign_Up(request):
    '''Teacher_Sign_Up'''
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

    return render(request,'classroom/teacher_signup.html',{'user_form':user_form,
        'teacher_profile_form':teacher_profile_form,'registered':registered,'user_type':user_type})


def Student_Sign_Up(request):
    '''Student_Sign_Up'''
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

    return render(request,'classroom/student_signup.html',{'user_form':user_form,
    'student_profile_form':student_profile_form,'registered':registered,'user_type':user_type})

def Sign_Up(request):
    '''Sign_Up'''
    return render(request,'classroom/signup.html',{})


## login view.
def user_login(request):
    '''user_login'''
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
    '''user_logout'''
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def change_password(request):
    '''change_password'''
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
def write_message(request,pk):
    '''write_message'''
    message_sent = False
    teacher = get_object_or_404(models.Teacher,pk=pk)

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            mssg = form.save(commit=False)
            mssg.teacher = teacher
            mssg.student = request.user.Student
            mssg.save()
            message_sent = True
    else:
        form = MessageForm()
    return render(request,'classroom/write_message.html',
                  {'form':form,'teacher':teacher,'message_sent':message_sent})

@login_required
def class_students_list(request):
    '''class_students_list'''
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
            qs_one.append(x)
        else:
            pass
    context = {
        "class_students_list": qs_one,
    }
    template = "classroom/class_students_list.html"
    return render(request, template, context)

class ClassStudentsListView(LoginRequiredMixin,DetailView):
    '''ClassStudentsListView'''
    model = models.Teacher
    template_name = "classroom/class_students_list.html"
    context_object_name = "teacher"

class StudentAllMsgList(LoginRequiredMixin, DetailView):
    '''StudentAllMsgList'''
    model = models.Student
    template_name = "classroom/student_allmsg_list.html"
    context_object_name = "student"


@login_required
def add_msg(request, pk):
    '''Add Message'''
    msg_given = False
    student = get_object_or_404(models.Student,pk=pk)
    if request.method == "POST":
        form = MsgForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.student = student
            msg.teacher = request.user.Teacher
            msg.save()
            messages.success(request,'Msg uploaded successfully!')
            return redirect('classroom:submit_list')
    else:
        form = MsgForm()
    return render(request,'classroom/add_msg.html',
    {'form':form,'student':student,'msg_given':msg_given})


@login_required
def update_msg(request, pk):
    '''update_msg'''
    msg_updated = False
    obj = get_object_or_404(StudentMsg,pk=pk)
    if request.method == "POST":
        form = MsgForm(request.POST,instance=obj)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.save()
            msg_updated = True
    else:
        form = MsgForm(request.POST or None,instance=obj)
    return render(request,'classroom/update_msg.html',{'form':form,'msg_updated':msg_updated})


@login_required
def class_notice(request,pk):
    '''class_notice'''
    student = get_object_or_404(models.Student,pk=pk)
    return render(request,'classroom/class_notice_list.html',{'student':student})



@login_required
def add_notice(request):
    '''add_notice'''
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



@login_required
def students_list1(request):
    '''students_list'''
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

def teachers_list(request):
    '''teachers_list'''
    query = request.GET.get("q", None)
    qs = Teacher.objects.all()
    if query is not None:
        qs = qs.filter(
                Q(subject_name__icontains=query)
                )
    context = {
        "teachers_list": qs,
    }
    template = "classroom/teachers_list.html"
    return render(request, template, context)


class Student_All_Msg_List(LoginRequiredMixin, DetailView):
    '''Student_All_Msg_List'''
    model = models.Student
    template_name = "classroom/student_allmsg_list.html"
    context_object_name = "student"

@login_required
def student_msg_list(request, pk):
    ''''student_msg_list'''
    student = get_object_or_404(models.Student,pk=pk)
    teacher = request.user.Teacher
    given_msg = StudentMsg.objects.filter(teacher=teacher,student=student)
    return render(request,'classroom/student_msg_list.html',
                  {'student':student,'given_msg':given_msg})


@login_required
def class_file(request):
    '''class_file'''
    student = request.user.Student
    file = SubmitFile.objects.filter(student=student)
    file_list = [x.submitted_file for x in file]
    return render(request,'classroom/class_file.html',{'student':student,'file_list':file_list})

@login_required
def file_list(request):
    '''file_list'''
    teacher = request.user.Teacher
    return render(request,'classroom/file_list.html',{'teacher':teacher})

@login_required
def update_file(request, id=None):
    '''update_file'''
    obj = get_object_or_404(ClassFile, id=id)
    form = FileForm(request.POST or None, instance=obj)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        if 'file' in request.FILES:
            obj.file = request.FILES['file']
        obj.save()
        messages.success(request, "Updated File".format(obj.file_name))
        return redirect('classroom:file_list')
    template = "classroom/update_file.html"
    return render(request, template, context)

@login_required
def file_delete(request, id=None):
    '''file_delete'''
    obj = get_object_or_404(ClassFile, id=id)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "File Removed")
        return redirect('classroom:file_list')
    context = {
        "object": obj,
    }
    template = "classroom/file_delete.html"
    return render(request, template, context)


@login_required
def upload_file(request):
    '''upload_file'''
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
    template = "classroom/upload_file.html"
    return render(request,template,{'form':form,'file_uploaded':file_uploaded})

@login_required
def submit_file(request, id=None):
    '''submit_file'''
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
def messages_list(request,pk):
    '''messages_list'''
    teacher = get_object_or_404(models.Teacher,pk=pk)
    return render(request,'classroom/messages_list.html',{'teacher':teacher})


@login_required
def submit_list(request):
    '''submit_list'''
    teacher = request.user.Teacher
    return render(request,'classroom/submit_list.html',{'teacher':teacher})

@login_required
def massege_teach_admin(request):
    '''massege_teach_admin'''
    if request.method == 'POST':
        message1 = request.POST['message1']
        print(message1)
        obj = message_teach_admin()
        obj.message=message1
        obj.save()
    return render(request,'classroom/massege_teach_admin.html',{})
@login_required
def massage_student_admin(request):
    '''massage_student_admin'''
    if request.method == 'POST':
        message2 = request.POST['message2']
        print(message2)
        obj2 = message_student_admin()
        obj2.message=message2
        obj2.save()
    return render(request,'classroom/message_student_admin.html',{})
@login_required
def change_Salary_Demand(request):
    '''change_Salary_Demand'''
    if request.method == 'POST':
        salary = request.POST['Salary']
        username = request.POST['username1']
        print(salary)
        print(username)
        obj2 = Change_Salary_Demand()
        obj2.TeacherName = username
        obj2.salary = salary
        obj2.save()
    context={}
    return render(request,'classroom/Change_Salary_Demand.html',context)
def Contact_Us(request):
    '''Contact_Us'''
    if request.method=="POST":
        name=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        subject=request.POST['subject']
        desc=request.POST['desc']
        obj2 = Contact()
        obj2.name=name
        obj2.email=email
        obj2.phone=phone
        obj2.subject=subject
        obj2.desc=desc
        obj2.save()
    return render(request,'classroom/contact.html',{})


class Student_Detail_View(LoginRequiredMixin, DetailView):
    '''Student_Detail_View'''
    context_object_name = "student"
    model = models.Student
    template_name = 'classroom/student_detail_page.html'

class Teacher_Detail_View(LoginRequiredMixin,DetailView):
    '''Teacher_Detail_View'''
    context_object_name = "teacher"
    model = models.Teacher
    template_name = 'classroom/teacher_detail_page.html'


@login_required
def Teacher_Update_View(request,pk):
    '''asd'''
    profile_updated = False
    teacher = get_object_or_404(models.Teacher,pk=pk)
    if request.method == "POST":
        form = TeacherProfileUpdateForm(request.POST,instance=teacher)
        if form.is_valid():
            profile = form.save(commit=False)
            if 'teacher_profile_pic' in request.FILES:
                profile.teacher_profile_pic = request.FILES['teacher_profile_pic']
            profile.save()
            profile_updated = True
    else:
        form = TeacherProfileUpdateForm(request.POST or None,instance=teacher)
    return render(request,'classroom/teacher_update_page.html',
                  {'profile_updated':profile_updated,'form':form})

class add_student(LoginRequiredMixin,generic.RedirectView):
    '''asd'''
    def get_redirect_url(self,*args,**kwargs):
        '''asd'''
        return reverse('classroom:students_list')

    def get(self,request,*args,**kwargs):
        '''asd'''
        student = get_object_or_404(models.Student,pk=self.kwargs.get('pk'))

        try:
            StudentsInClass.objects.create(teacher=self.request.user.Teacher,student=student)
        except:
            messages.warning(self.request,'warning, Student already in class!')
        else:
            messages.success(self.request,'{} successfully added!'.format(student.name))

        return super().get(request,*args,**kwargs)


def users_alert_messages(request):
    '''users_alert_messages'''
    objs = alert_for_users.objects.all()
    context = {'objs': objs}
    return render(request, "classroom/alert.html", context)



@login_required
def Student_Update_View(request,pk):
    '''Student_Update_View'''
    profile_updated = False
    student = get_object_or_404(models.Student,pk=pk)
    if request.method == "POST":
        form = StudentProfileUpdateForm(request.POST,instance=student)
        if form.is_valid():
            profile = form.save(commit=False)
            if 'student_profile_pic' in request.FILES:
                profile.student_profile_pic = request.FILES['student_profile_pic']
            profile.save()
            profile_updated = True
    else:
        form = StudentProfileUpdateForm(request.POST or None,instance=student)
    return render(request,'classroom/student_update_page.html',
                  {'profile_updated':profile_updated,'form':form})
