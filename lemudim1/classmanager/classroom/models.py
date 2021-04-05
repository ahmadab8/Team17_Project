from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Teacher(models.Model):

    user = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    Age = models.CharField(max_length=10)
    per_hour = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

 #teacher_profile_pic = models.ImageField(upload_to="classroom/teacher_profile_pic", blank=True)
 #description = models.TextField()
 #schedule = models.CharField(max_length=250)
    def __str__(self):
        return self.name
class Student(models.Model):

    user = models.CharField(max_length=20, primary_key=True)
    Last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    first_name = models.CharField(max_length=10)

    password = models.CharField(max_length=50)



class Register_Teacher(models.Model):

    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=50)