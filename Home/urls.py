from django.urls import path
from .views import HomeView,CourseView,InstructorView,About_usView,ContactUsView,PortfolioView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('course',CourseView.as_view(),name='courses'),
    path('course/<uuid:course_id>',CourseView.as_view(),name='single_course'),
    path('instructors',InstructorView.as_view(),name='instructors'),
    path('instructors/<int:instructor_id>',InstructorView.as_view(),name='single_instructor'),
    path('about_us',About_usView.as_view(),name='about_us'),
    path('contact_us',ContactUsView.as_view(),name='contact_us'),
    path('portfolio',PortfolioView.as_view(),name='portfolio'),
    path('portifolio_details/<uuid:id>',PortfolioView.as_view(),name='portifolio_details'),
]