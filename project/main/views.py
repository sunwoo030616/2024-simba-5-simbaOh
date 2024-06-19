from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Mentor



def intro(request):
    return render(request, 'main/intro.html')

def first_screen(request):
    return render(request, 'main/first_screen.html')

def mainpage(request):
    return render(request, 'main/mainpage.html')

def mentor_start(request):
    return render(request, 'main/mentor_start.html')

def mentor_list(request):
    mentors = Mentor.objects.all()
    return render(request, 'main/mentor_list.html', {'mentors' : mentors})

def mentor_enroll(request):
    return render(request, 'main/mentor_enroll.html')

def mentor_info(request, id):
    mentor = get_object_or_404(Mentor, pk = id)
    return render(request, 'main/mentor_info.html', {'mentor' : mentor})


def mentor_create(request):
        new_mentor = Mentor()

        new_mentor.mentor_name = request.user

        new_mentor.mentor_company = request.POST['mentor_company']
        new_mentor.mentor_dept = request.POST['mentor_dept']
        new_mentor.mentor_work = request.POST['mentor_work']

        new_mentor.mentor_intro = request.POST['mentor_intro']
        new_mentor.mentor_year = request.POST['mentor_year']

        new_mentor.mentor_at = timezone.now()

        new_mentor.save()
        return redirect('main:mentor-list')

<<<<<<< HEAD
def mentor_ask(request):
    return render(request, 'main/mentor_ask.html')
=======

>>>>>>> 509426d45bf1994b8eb46519842a1a1be4be9ad5
