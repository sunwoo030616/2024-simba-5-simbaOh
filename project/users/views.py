from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Portfolio, Education, Experience, Project, Certification
from accounts.models import Profile
from main.models import Mentor
from community.models import Free, Move
from careers.models import Careerinfo


def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    profile, created = Profile.objects.get_or_create(user=user)
    portfolio, created = Portfolio.objects.get_or_create(user=user)
    following_count = user.mentor_followings.count()

    context = {
        'user': user,
        'profile': profile,
        'portfolio': portfolio,
        'following_count': following_count,
    }
    
    return render(request, 'users/mypage.html', context)

def follow_list(request, id):
    user = get_object_or_404(User, pk=id)
    context = {
        'followings': user.mentor_followings.all()
    }
    return render(request, 'users/follow_list.html', context)

def bookmark(request, id):
    return render(request, 'users/bookmark.html')

def edit_portfolio(request):
    portfolio, created = Portfolio.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        introduction = request.POST.get('introduction')
        education_list = request.POST.getlist('education')
        experience_list = request.POST.getlist('experience')
        projects_list = request.POST.getlist('projects')
        certifications_list = request.POST.getlist('certifications')

        portfolio.title = title
        portfolio.introduction = introduction

        portfolio.education.clear()
        for edu in education_list:
            education, created = Education.objects.get_or_create(name=edu)
            portfolio.education.add(education)

        portfolio.experience.clear()
        for exp in experience_list:
            experience, created = Experience.objects.get_or_create(name=exp)
            portfolio.experience.add(experience)

        portfolio.projects.clear()
        for proj in projects_list:
            project, created = Project.objects.get_or_create(name=proj)
            portfolio.projects.add(project)

        portfolio.certifications.clear()
        for cert in certifications_list:
            certification, created = Certification.objects.get_or_create(name=cert)
            portfolio.certifications.add(cert)

        portfolio.save()

        return redirect('users:mypage', id=request.user.id)

    return render(request, 'users/edit_portfolio.html', {'portfolio': portfolio})

# def update_profile(request, id):
#     update_profile = Profile.objects.get(pk=id)
#     if request.user.is_authenticated and request.user == update_profile.user:
#         update_profile.user_name = request.POST['user_name']
#         update_profile.user_phone = request.POST['user_phone']
#         update_profile.user_birth = request.POST['user_birth']

#         update_profile.user_major = request.POST['user_major']
#         update_profile.user_enroll = request.POST['user_enroll']
        
#         if request.FILES.get('user_profile'):
#             update_profile.user_profile = request.FILES.get('user_profile')

#         update_profile.save()

#         return redirect('main:mainpage', id)
#     return render(request, 'users/update_profile.html')

def my_writing(request, id):
    user = User.objects.get(pk=id)
    username = request.user
    my_writes_free = Free.objects.filter(writer = username)
    my_writes_move = Move.objects.filter(writer = username)
    my_writes_careerinfo = Careerinfo.objects.filter(writer = username)
    context = {
        'user' : user,
        'my_writes_free' : my_writes_free,
        'my_writes_move' : my_writes_move,
        'my_writes_careerinfo' : my_writes_careerinfo
    }
    return render(request, 'users/my_writing.html', context)

def mentoring(request, id):
    return render(request, 'users/mentoring.html')

def career_now(request, id):
    return render(request, 'users/career_now.html')

def cibm_list(request):
    user = request.user
    cibms = user.ci_bms.all()
    return render(request, 'users/cibm.html', {'cibms': cibms})
