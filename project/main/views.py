from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Mentor
from django.contrib.auth.models import User
from accounts.models import Profile

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
    profiles = Profile.objects.all()
    return render(request, 'main/mentor_list.html', {
        'mentors' : mentors,
        'profiles' : profiles
        })

def mentor_enroll(request):
    return render(request, 'main/mentor_enroll.html')

def mentor_info(request, id):
    user = get_object_or_404(User, pk=id)
    profile = get_object_or_404(Profile, user=user)
    profile, created = Profile.objects.get_or_create(user=user)
    return render(request, 'main/mentor_info.html', {
        'user' : user,
        'profile' : profile
    })


def mentor_create(request):
    if request.user.is_authenticated:
        new_mentor = Mentor()

        new_mentor.user = request.user

        new_mentor.mentor_company = request.POST['mentor_company']
        new_mentor.mentor_dept = request.POST['mentor_dept']
        new_mentor.mentor_work = request.POST['mentor_work']

        new_mentor.mentor_summary = request.POST['mentor_summary']
        new_mentor.mentor_info = request.POST['mentor_info']
        new_mentor.mentor_career = request.POST['mentor_career']
        new_mentor.mentor_certificate = request.POST['mentor_certificate']
        new_mentor.mentor_id_card = request.FILES.get('image_1')
        new_mentor.mentor_name_card = request.FILES.get('image_2')

        new_mentor.mentor_at = timezone.now()

        new_mentor.save()
        return redirect('main:mentor-list')
    else:
        return render(request, 'main/mentor_enroll.html')

def mentor_ask(request):
    return render(request, 'main/mentor_ask.html')
