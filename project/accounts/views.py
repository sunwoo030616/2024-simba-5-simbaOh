from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def login(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']

        user = auth.authenticate(request, username=user_id, password=user_pw)

        if user is not None:
            auth.login(request, user)
            return render(request, 'main:mainpage')
        else:
            return render(request, 'accounts/login.html')

    elif request.method == 'GET':
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('main:mainpage')

def signup(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']

        if request.POST['user_pw'] == request.POST['confirm']:
            user = User.objects.create_user(
                username=request.POST['user_id'],
                password=request.POST['user_pw']
            )
            user_name = request.POST['user_name']
            user_phone = request.POST['user_phone']
            user_birth = request.POST['user_birth']

            user_major = request.POST['user_major']
            user_profile = request.FILES.get('user_profile')
            user_enroll = request.POST['user_enroll']
            
            
            profile = Profile(user=user, user_name=user_name,  user_phone=user_phone,  user_birth=user_birth, user_major=user_major, user_profile=user_profile,user_enroll=user_enroll, )
            profile.save()

            auth.login(request, user)
            return redirect('/')
        
    return render(request, 'accounts/signup.html')