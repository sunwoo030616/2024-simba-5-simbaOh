from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Portfolio
from django.contrib.auth.models import User
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
        education = request.POST.get('education')
        experience = request.POST.get('experience')
        projects = request.POST.get('projects')
        certifications = request.POST.get('certifications')

        portfolio.title = title
        portfolio.introduction = introduction
        portfolio.education = education
        portfolio.experience = experience
        portfolio.projects = projects
        portfolio.certifications = certifications
        portfolio.save()

        return redirect('users:mypage', id=request.user.id)

    return render(request, 'users/edit_portfolio.html', {'portfolio': portfolio})