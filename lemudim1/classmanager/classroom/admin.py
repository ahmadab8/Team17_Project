'''admin rules'''
# pylint: disable=E0402
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Student,Teacher,message_teach_admin,message_student_admin,\
    MessageToTeacher,StudentsInClass,ClassNotice,Change_Salary_Demand,alert_for_users,Contact
# Register your models here.


admin.site.register(User, UserAdmin)
#students list
admin.site.register(Student)
#messages that sent to admin by teachers
admin.site.register(message_teach_admin)
#messages that sent by students to admin
admin.site.register(message_student_admin)
#msg between boy/girl school and teacher
admin.site.register(MessageToTeacher)
#msg between teachers and boy/girl school
admin.site.register(ClassNotice)
#teachers list
admin.site.register(Teacher)
admin.site.register(StudentsInClass)
admin.site.register(Change_Salary_Demand)
#alerts messages to website users
admin.site.register(alert_for_users)
#message from contact
admin.site.register(Contact)
admin.site.site_url = None
admin.site.site_header = 'Welcome to Our Website'
admin.site.index_title = 'Admin tools'
