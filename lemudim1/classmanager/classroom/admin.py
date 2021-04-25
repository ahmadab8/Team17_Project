from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Student,Teacher,message_teach_admin,message_student_admin
# Register your models here.


admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(message_teach_admin)
admin.site.register(message_student_admin)
