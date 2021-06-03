'''db'''
# pylint: disable=R0903,C0103,C0304,E0602,E1101,E0402,C0305
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
import misaka

# Create your models here.



class User(AbstractUser):
    '''User'''
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    '''Student'''
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True, related_name='Student')
    name = models.CharField(max_length=250)
    student_of = models.CharField(max_length=250)
    language = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=250)
    student_profile_pic = models.ImageField(upload_to="classroom/student_profile_pic", blank=True)

    def get_absolute_url(self):
        '''asd'''
        return reverse('classroom:student_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name.__str__()

    class Meta:
        '''meta'''
        ordering = ['language']


class Teacher(models.Model):
    '''Teacher'''
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True, related_name='Teacher')
    name = models.CharField(max_length=250)
    subject_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=250)
    money_per_hour = models.CharField(max_length=250)
    teacher_profile_pic = models.ImageField(upload_to="classroom/teacher_profile_pic", blank=True)
    class_students = models.ManyToManyField(Student, through="StudentsInClass")
    description = models.TextField()
    payment_way = models.CharField(max_length=250)
    schedule = models.CharField(max_length=250)

    def get_absolute_url(self):
        '''asd'''
        return reverse('classroom:teacher_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name.__str__()


class StudentsInClass(models.Model):
    '''StudentsInClass'''
    teacher = models.ForeignKey(Teacher, related_name="class_teacher", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name="user_student_name", on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name

    class Meta:
        '''meta'''
        unique_together = ('teacher', 'student')


class StudentMsg(models.Model):
    '''Student Message'''
    teacher = models.ForeignKey(Teacher, related_name='given_msg', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name="msg", on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=250)
    msg_obtained = models.TextField()

    def __str__(self):
        return self.subject_name.__str__()




class ClassNotice(models.Model):
    '''ClassNotice'''
    teacher = models.ForeignKey(Teacher, related_name='teacher', on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='class_notice')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)

    def __str__(self):
        return self.message.__str__()

    def save(self, *args, **kwargs):
        '''save'''
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    class Meta:
        '''meta'''
        ordering = ['-created_at']
        unique_together = ['teacher', 'message']



#msg between student and teacher
class MessageToTeacher(models.Model):
    '''MessageToTeacher'''
    student = models.ForeignKey(Student, related_name='student', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, related_name='messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)

    def __str__(self):
        return self.message.__str__()

    def save(self, *args, **kwargs):
        '''save'''
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    class Meta:
        '''Meta'''
        ordering = ['-created_at']
        unique_together = ['student', 'message']



class ClassFile(models.Model):
    '''ClassFile'''
    student = models.ManyToManyField(Student, related_name='student_file')
    teacher = models.ForeignKey(Teacher, related_name='teacher_file', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    file_name = models.CharField(max_length=250)
    file = models.FileField(upload_to='files')

    def __str__(self):
        return self.file_name.__str__()

    class Meta:
        '''Meta'''
        ordering = ['-created_at']


class SubmitFile(models.Model):
    '''SubmitFile'''
    student = models.ForeignKey(Student, related_name='student_submit', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, related_name='teacher_submit', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    submitted_file = models.ForeignKey(ClassFile, related_name='submission_for_file',
                                       on_delete=models.CASCADE)
    submit = models.FileField(upload_to='Submission')

    def __str__(self):
        return "Submitted" + str(self.submitted_file.file_name)

    class Meta:
        '''Meta'''
        ordering = ['-created_at']


class message_teach_admin(models.Model):
    '''message_teach_admin'''
   # teacher = models.ForeignKey(Teacher, related_name='messages', on_delete=models.CASCADE)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.message.__str__()
class Change_Salary_Demand(models.Model):
    '''message_teach_admin'''
   # teacher = models.ForeignKey(Teacher, related_name='messages', on_delete=models.CASCADE)
    TeacherName = models.CharField(max_length=50)
    salary = models.CharField(max_length=20)
    def __str__(self):
        return self.TeacherName.__str__()



class message_student_admin(models.Model):
    '''message_teach_admin'''
   # teacher = models.ForeignKey(Teacher, related_name='messages', on_delete=models.CASCADE)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.message.__str__()


class alert_for_users(models.Model):
    '''message_teach_admin'''
   # teacher = models.ForeignKey(Teacher, related_name='messages', on_delete=models.CASCADE)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.message.__str__()

class Contact(models.Model):
    '''message_teach_admin'''
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    subject = models.CharField(max_length=250)
    desc = models.TextField()

    def __str__(self):
        return self.name + ", subject: " + self.subject