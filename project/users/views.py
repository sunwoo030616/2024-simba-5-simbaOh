from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Portfolio, Education, Experience, Project, Certification
from accounts.models import Profile
from main.models import Mentor


def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    profile, created = Profile.objects.get_or_create(user=user)
    portfolio, created = Portfolio.objects.get_or_create(user=user)

    return render(request, 'users/mypage.html', {
        'user': user,
        'profile': profile,
        'portfolio': portfolio
    })

def follow_list(request, id):
    user = get_object_or_404(User, pk=id)
    context = {
        'user':user,
        'followers': user.profile.followers.all(),
        'followings': user.profile.followings.all()
    }
    return render(request, 'users/follow_list.html', context)

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
