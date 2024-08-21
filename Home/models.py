from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field
import uuid
# Create your models here.
class Software(models.Model):
    name=models.CharField(max_length=255)
    thumbnail=models.ImageField(upload_to='software_thumbnails')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('-created_at',)
class Actions(models.Model):
    thumbnail=models.ImageField(upload_to='actions_thumbnails')  
    created_at=models.DateTimeField(auto_now_add=True,null=True) 

   
    class Meta:
        ordering = ('-created_at',)
class Awards(models.Model):
    award_image=models.ImageField(upload_to='awards_thumbnails')
    award_title=models.CharField(max_length=255) 
    award_description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.award_title
    class Meta:
        verbose_name_plural = 'Awards'
        ordering = ('-created_at',)  
class Event(models.Model):
    event_image=models.ImageField(upload_to='event_thumbnails')
    event_title=models.CharField(max_length=255)
    event_description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.event_title    
    class Meta:
        verbose_name_plural = 'Events'
        ordering = ('-created_at',) 

class Testimonials(models.Model):
    testimonial_image=models.ImageField(upload_to='testimonials_thumbnails')
    testimonial_name=models.CharField(max_length=255)
    testimonial_description=models.TextField()
    testimonial_position=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True,null=True)    
    def __str__(self):
        return self.testimonial_name
    class Meta:
        verbose_name_plural = 'Testimonials'  
        ordering = ('-created_at',)   
class Team(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    position=models.CharField(max_length=255)
    profile=models.ImageField(upload_to='Team_profile',null=True)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)             

    def __str__(self):
        return self.user.username
class Portfolio(models.Model):
    id=models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4())
    portfolio_image=models.ImageField(upload_to='portfolio_thumbnails')
    portfolio_title=models.CharField(max_length=255)
    portfolio_description=CKEditor5Field(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.portfolio_title
