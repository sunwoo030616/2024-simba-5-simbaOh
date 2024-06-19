from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Portfolio
from django.contrib.auth.models import User
from accounts.models import Profile

def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    profile = get_object_or_404(Profile, user=user)
    profile, created = Profile.objects.get_or_create(user=user)
    portfolio, created = Portfolio.objects.get_or_create(user=user)

    return render(request, 'users/mypage.html', {
        'user': user,
        'profile': profile,
        'portfolio': portfolio
    })

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