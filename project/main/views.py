from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Mentor, Category, Relation_mentor, Menti
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
    category_list = [
            '인사/노무',
            'IT개발/데이터',
            '디자인',
            '영상/판매/무역',
            '상품기획/MD',
            '서비스',
            '생산',
            '의료',
            '건설/건축',
            '연구/R&D',
            '교육',
            '금융/보험',
            '미디어/스포츠',
            '교육'
        ]
    if request.method == 'POST':
        selected_categories = request.POST.getlist('categories')
        if selected_categories:
            selected_category_names = [category_list[int(i)] for i in selected_categories]
            mentors = Mentor.objects.filter(mentor_work__in=selected_category_names)
            return render(request, 'main/mentor_list.html', {'mentors': mentors})
        else:
            mentors = Mentor.objects.all()
            return render(request, 'main/mentor_list.html', {'mentors': mentors})
    else:
        mentors = Mentor.objects.all()
    return render(request, 'main/mentor_list.html', {'mentors': mentors})

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
        new_mentor.mentor_id_card = request.FILES.get('image_1')
        new_mentor.mentor_name_card = request.FILES.get('image_2')
        new_mentor.mentor_at = timezone.now()

        new_mentor.save()
        return redirect('main:mentor-list')
    else:
        return redirect('main:first-screen')

def mentor_info(request, id):
    mentor = get_object_or_404(Mentor, pk = id)
    return render(request, 'main/mentor_info.html', {'mentor' : mentor})

def mentor_relation_create(request, id):
    user=request.user
    mentor = get_object_or_404(Mentor, pk=id)
    new_relation = Relation_mentor()
    new_relation.mentor = mentor
    new_relation.menti = user
    new_relation.state = ''
    new_relation.mentoring_at = timezone.now()
    new_relation.save()

    return redirect('main:mentor-info', mentor.id)

def mentor_ask(request, id):
    user = request.user
    mentor = get_object_or_404(Mentor, pk = id)
    menti = Menti.objects.all()
    is_mentoring = user in mentor.mentor_ship.all()
    if mentor.user == request.user:
        return redirect('main:mentor-list')
    else:
        if is_mentoring:
            mentor.mentor_ship.remove(user)
            menti.delete
            return redirect('main:mentor-info', mentor.id)
        else:
            return render(request, 'main/mentor_ask.html', {'mentor':mentor})

def create_menti(request, id):
    user = request.user
    mentor = get_object_or_404(Mentor, pk=id)
    new_menti = Menti()
    new_menti.user = user
    new_menti.mentor = mentor
    new_menti.summary = request.POST['summary']
    new_menti.content = request.POST['content']
    new_menti.save()
    mentor.mentor_ship.add(user)
    return redirect('main:mentor-relation-create', mentor.id)

def follow(request, id):
    user = request.user
    mentor = get_object_or_404(Mentor, pk=id)
    is_follower = user in mentor.followers.all()
    if is_follower:
        mentor.followers.remove(user)
    else:
        mentor.followers.add(user)
    return redirect('main:mentor-info', mentor.id)

def follow2(request, id):
    user = request.user
    mentor = get_object_or_404(Mentor, pk=id)
    is_follower = user in mentor.followers.all()
    if is_follower:
        mentor.followers.remove(user)
    else:
        mentor.followers.add(user)
    return redirect('users:follow-list', user.id)
