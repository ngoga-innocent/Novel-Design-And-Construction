from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field
import uuid
# Create your models here.
class Instructors(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    position=models.CharField(max_length=255,default='NDC Instructor')
    specialization=models.CharField(max_length=255,default='Construction Softwares')
    profile_image=models.ImageField(upload_to='instructors_profile',null=True)
    description=CKEditor5Field(null=True,blank=True)
    joined_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name_plural = 'Instructors'

class Course(models.Model):
    id=models.UUIDField(primary_key=True,editable=False,null=False,default=uuid.uuid4)
    title=models.CharField(max_length=255)
    description=models.TextField()
    teacher_course_description=CKEditor5Field(null=True,blank=True)
    whocanjoin=CKEditor5Field(null=True,blank=True)
    thumbnail=models.ImageField(upload_to='Course/Thumbnails',null=True, blank=True)
    lecture=models.ForeignKey(Instructors, on_delete=models.SET_NULL,null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Student(models.Model):
    id=models.UUIDField(primary_key=True,editable=False,null=False,default=uuid.uuid4) 
    First_Name=models.CharField(max_length=255,null=False)
    Middle_Name=models.CharField(max_length=255)
    Last_Name=models.CharField(max_length=255,null=False)
    phone_number=models.CharField(max_length=255,null=False)
    email=models.EmailField(null=True)
    course=models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
    accepted=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)   

    def __str__(self):
        return f"" +self.First_Name+" " + self.Last_Name
    class Meta:
        ordering=("-created_at",)
        verbose_name_plural = 'Students'
    
