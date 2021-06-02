from .models import *


class auth:
    def student_register(self,student):
        student.save()
    def teacher_register(self,teacher):
        teacher.save()
    def delete_student(req,student):
        Student.delete(student)
    def delete_teacher(req,teacher):
        Teacher.delete(teacher)
    def change_password(self,oldpassword,newpassword,user):
        if user.check_password(oldpassword):
            user.set_password(newpassword)
            user.save()
            return True
        return False