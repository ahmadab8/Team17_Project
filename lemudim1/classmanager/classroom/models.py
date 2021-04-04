from django.db import models




# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    username = models.CharField(max_length=250)
    per_hour = models.CharField(max_length=250)
    Age = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)

