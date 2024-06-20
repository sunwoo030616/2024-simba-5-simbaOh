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
    if request.method == 'POST':
        new_mentor = Mentor()
        new_mentor.user = request.user
        new_mentor.mentor_company = request.POST.get('mentor_company', '')
        new_mentor.mentor_dept = request.POST.get('mentor_dept', '')
        new_mentor.mentor_work = request.POST.get('mentor_work', '')
        new_mentor.mentor_info = request.POST.get('mentor_info', '')
        new_mentor.mentor_career = request.POST.get('mentor_career', '')
        new_mentor.mentor_summary = request.POST.get('mentor_summary', '')  # 누락된 필드 추가
        new_mentor.mentor_certificate = request.POST.get('mentor_certificate', '')

        if 'mentor_id_card' in request.FILES:
            new_mentor.mentor_id_card = request.FILES['mentor_id_card']
        if 'mentor_name_card' in request.FILES:
            new_mentor.mentor_name_card = request.FILES['mentor_name_card']

        new_mentor.mentor_at = timezone.now()
        new_mentor.save()
        return redirect('main:mentor-list')
    return render(request, 'main/mentor_enroll.html')

def mentor_ask(request):
    return render(request, 'main/mentor_ask.html')
