from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Mentor
from django.contrib.auth.models import User


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
        new_mentor.mentor_id_card = request.FILES['image_1']
        new_mentor.mentor_name_card = request.FILES['image_2']
        new_mentor.mentor_at = timezone.now()

        new_mentor.save()
        return redirect('main:mentor-list')
    else:
        return redirect('main:first-screen')

def mentor_info(request, id):
    mentor = get_object_or_404(Mentor, pk = id)
    return render(request, 'main/mentor_info.html', {'mentor' : mentor})

# @login_required
# def mentor_enroll(request):
#     if request.method == 'POST':
#         mentor_company = request.POST.get('mentor_company', '')
#         mentor_dept = request.POST.get('mentor_dept', '')
#         mentor_work = request.POST.get('mentor_work', '')

#         # Mentor 객체가 없으면 생성
#         if not hasattr(request.user, 'mentor'):
#             mentor = Mentor.objects.create(
#                 user=request.user,
#                 mentor_company=mentor_company,
#                 mentor_dept=mentor_dept,
#                 mentor_work=mentor_work,
#                 mentor_at=timezone.now()
#             )
#         else:
#             mentor = request.user.mentor
#             mentor.mentor_company = mentor_company
#             mentor.mentor_dept = mentor_dept
#             mentor.mentor_work = mentor_work
#             mentor.save()
#             request.session['mentor_id'] = mentor.id
#         return redirect('main:mentor-enroll2')
#     return render(request, 'main/mentor_enroll.html')

# @login_required
# def mentor_enroll2(request):
#     if request.method == 'POST':
#         mentor_summary = request.POST.get('mentor_summary', '')
#         mentor_info = request.POST.get('mentor_info', '')
#         mentor_career = request.POST.get('mentor_career', '')
#         mentor_certificate = request.POST.get('mentor_certificate', '')

#         mentor_id = request.session.get('mentor_id')
#         if mentor_id:
#             mentor = Mentor.objects.get(id=mentor_id)
#             mentor.mentor_summary = mentor_summary
#             mentor.mentor_info = mentor_info
#             mentor.mentor_career = mentor_career
#             mentor.mentor_certificate = mentor_certificate
#             mentor.save()
#         return redirect('main:mentor-enroll3')
#     return render(request, 'main/mentor_enroll2.html')

# @login_required
# def mentor_enroll3(request):
#     if request.method == 'POST':
#         mentor_id_card = request.FILES.get('mentor_id_card')
#         mentor_name_card = request.FILES.get('mentor_name_card')

#         mentor_id = request.session.get('mentor_id')
#         if mentor_id:
#             mentor = Mentor.objects.get(id=mentor_id)
#             if mentor_id_card:
#                 mentor.mentor_id_card = mentor_id_card
#             if mentor_name_card:
#                 mentor.mentor_name_card = mentor_name_card
#             mentor.save()
#         return redirect('main:mentor-list')
#     return render(request, 'main/mentor_enroll3.html')

def mentor_ask(request, id):
    mentor = get_object_or_404(Mentor, pk = id)
    if mentor.user == request.user:
        return redirect('main:mentor-list')
    return render(request, 'main/mentor_ask.html', {'mentor':mentor})

def follows(request, mentor_id):
    mentor = get_object_or_404(Mentor, pk = mentor_id)
    if request.user in mentor.follow.all():
        mentor.follow.remove(request.user)
        mentor.follow_count -= 1
        mentor.save()
    else:
        mentor.follow.add(request.user)
        mentor.follow_count += 1
        mentor.save()
    return redirect('main:mentor-info', mentor.id)
