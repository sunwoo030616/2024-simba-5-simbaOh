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


def mentor_enroll(request):
    if request.method == 'POST':
        request.session['mentor_company'] = request.POST.get('mentor_company', '')
        request.session['mentor_dept'] = request.POST.get('mentor_dept', '')
        request.session['mentor_work'] = request.POST.get('mentor_work', '')

        print("Step 1 Session Data:")
        print(request.session['mentor_company'])
        print(request.session['mentor_dept'])
        print(request.session['mentor_work'])
        return redirect('main:mentor-enroll2')
    return render(request, 'main/mentor_enroll.html')

def mentor_enroll2(request):
    if request.method == 'POST':
        request.session['mentor_summary'] = request.POST.get('mentor_summary', '')
        request.session['mentor_info'] = request.POST.get('mentor_info', '')
        request.session['mentor_career'] = request.POST.get('mentor_career', '')
        request.session['mentor_certificate'] = request.POST.get('mentor_certificate', '')
        return redirect('main:mentor-enroll3')
    return render(request, 'main/mentor_enroll2.html')

def mentor_enroll3(request):
    if request.method == 'POST':
        request.session['mentor_id_card'] = request.FILES.get('mentor_id_card')
        request.session['mentor_name_card'] = request.FILES.get('mentor_name_card')
        return redirect('main:mentor-create')
    return render(request, 'main/mentor_enroll3.html')

def mentor_ask(request):
    return render(request, 'main/mentor_ask.html')
