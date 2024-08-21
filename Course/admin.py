from django.contrib import admin
from .models import Course,Instructors,Student
# Register your models here.
admin.site.register(Course)
admin.site.register(Instructors)
admin.site.register(Student)