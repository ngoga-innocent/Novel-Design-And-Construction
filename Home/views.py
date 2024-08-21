from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Software,Actions,Awards,Event,Testimonials,Team,Portfolio
from Course.models import Course,Student,Instructors
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.
class HomeView(View):
    def get(self,request):
        softwares = Software.objects.all()[:6]
        courses=Course.objects.all()[:5]
        actions=Actions.objects.all()[:5]
        award=Awards.objects.all()[:1]
        event=Event.objects.all()[:1]
        testimonials=Testimonials.objects.all()[:6]
        context={"softwares":softwares,"courses":courses,"actions":actions,"award":award,"events":event,"testimonials":testimonials}
        return render(request,'home.html',context)
class CourseView(View):
    def get(self,request,course_id=None):
        if not course_id:
            courses=Course.objects.all()
            context={"courses":courses}
            return render(request,'course.html',context) 
        else:
            try:
                course=Course.objects.get(id=course_id)
                context={"course":course}
                return render(request,'course-details.html',context)
            except Course.DoesNotExist:
                courses=Course.objects.all()
                context={"courses":courses}
                return render(request,'courses.html',context)
    def post(self,request):
        course_id = request.POST.get('course_id')
        
        if course_id:
            try:
                course = Course.objects.get(id=course_id)
            except Course.DoesNotExist:
                return JsonResponse({"error": "Course not found"}, status=404)

            first_name = request.POST.get('first_name')
            middle_name = request.POST.get('middle_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            print(first_name, middle_name)
            if not first_name or not last_name or not phone:
                print("emoty fields")
                return JsonResponse({"error": "First name, last name, and phone are required"}, status=400)

            try:
                student = Student.objects.create(
                    First_Name=first_name,
                    Middle_Name=middle_name,
                    Last_Name=last_name,
                    email=email,
                    phone_number=phone,
                    course=course
                )
                print("Student created")
                return JsonResponse({"details": "Student Saved"}, status=200)
            except Exception as e:
                print(str(e))
                return JsonResponse({"error": str(e)}, status=500)
        else:
            print("course id not availabele")
            return JsonResponse({"error": "Course ID is required"}, status=400)
class InstructorView(View):
    def get(self,request,instructor_id=None):
        if not instructor_id:
            instructors=Instructors.objects.all()
            context={"instructors":instructors}
            return render(request,'instructors.html',context) 
        else:
            try:
                instructor=Instructors.objects.get(id=instructor_id)
                context={"instructor":instructor}
                return render(request,'instructor-details.html',context)
            except Instructors.DoesNotExist:
                instructors=Instructors.objects.all()
                context={"instructors":instructors}
                return render(request,'instructors.html',context) 
class About_usView(View):
    def get(self,request):
        team_member=Team.objects.all()
        context={'team_members':team_member}
        return render(request,'about_us.html',context) 
class ContactUsView(View):
    def get(self,request):
        return render(request,'contact_us.html')   
    def post(self,request):
         
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        comment=request.POST.get('comment')
        context={
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "comment": comment,
        }
        html_message=render_to_string("email_template.html",context)
        plain_message = strip_tags(html_message)
        email=EmailMultiAlternatives(
            subject=f'new Contact Message from ' + first_name + ' ' + last_name,
            body=plain_message,
            from_email=None, 
            to=['ngogainnocent1@gmail.com']
        )
        email.attach_alternative(html_message, "text/html")
        email.send()
        # send_mail(f'new Contact Message from ' + first_name + ' ' + last_name,comment,email,['ngogainnocent1@gmail.com'])                 
        return JsonResponse(request.POST)
class PortfolioView(View):
    def get(self, request,id=None):
        portfolios=Portfolio.objects.all()
        if id is not None:
            try:
                portfolio=Portfolio.objects.get(id=id)
                return render(request,'single_portfolio.html',{"portfolio":portfolio})
            except Portfolio.DoesNotExist:
                return render(request,'portfolio.html',{"portfolios":portfolios})    
            
        
        return render(request,'portfolio.html',{"portfolios":portfolios})    