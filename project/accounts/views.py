from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def login(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']

        user = auth.authenticate(request, user_id=user_id, user_pw=user_pw)

        if user is not None:
            auth.login(request, user)
            return redirect('main:mainpage')
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
            
            
            
            profile = Profile(user=user)
            profile.save()

            auth.login(request, user)
            return redirect('/')
        
    return render(request, 'accounts/signup.html')