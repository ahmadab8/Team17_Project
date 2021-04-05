from django.shortcuts import render
from .models import Teacher, Student
from .models import Register_Teacher

# Create your views here.


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        user = request.POST['username']
        subject = request.POST['subject']
        Age = request.POST['Age']
        per_hour = request.POST['per_hour']
        password = request.POST['password']
        confirm = request.POST['confirm']
        print(name,email,user,subject,Age,per_hour,password,confirm)
        obj = Teacher()
        obj.name = name
        obj.email = email
        obj.per_hour = per_hour
        obj.Age = Age
        obj.subject = subject
        obj.user = user
        obj.password=password
        obj.save()

    context = {}
    return render(request,'signup.html',context)

def StudentSignUp(request):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            email = request.POST['email']
            user = request.POST['username']
            Last_name = request.POST['Last_name']
            password = request.POST['password']
            confirm = request.POST['confirm']
            print(Last_name, email, user, password, confirm)
            obj = Student()
            obj.first_name = first_name
            obj.email = email
            obj.Last_name =Last_name
            obj.user = user
            obj.password = password
            obj.save()

        context = {}
        return render(request, 'StudentSignUp.html', context)



def TeacherRegister(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        print(username, password, repassword)
        obj = Register_Teacher()
        obj.username = username
        obj.password = password
        obj.save()
    context = {}
    return render(request, 'TeacherRegister.html', context)