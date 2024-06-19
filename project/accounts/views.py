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
        user_name = request.POST['user_name']
        user_phone = request.POST['user_phone']
        user_birth = request.POST['user_birth']

        request.session['user_name'] = user_name
        request.session['user_phone'] = user_phone
        request.session['user_birth'] = user_birth

        return redirect('signup2')
    return render(request, 'accounts/signup.html')

def signup2(request):
    if request.method == 'POST':
        user_major = request.POST['user_major']
        user_enroll = request.POST['user_enroll']
        user_profile = request.FILES.get('user_profile')

        request.session['user_major'] = user_major
        request.session['user_enroll'] = user_enroll
        request.session['user_profile'] = user_profile

        return redirect('signup3')

    return render(request, 'accounts/signup2.html')

def signup3(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']

        if request.POST['user_pw'] == request.POST['confirm']:
            if User.objects.filter(username=user_id).exists():
                return render(request, 'accounts/signup.html', {'error': 'Username already exists'})
    
            user_name = request.session.get('user_name')
            user_phone = request.session.get('user_phone')
            user_birth = request.session.get('user_birth')
            user_major = request.session.get('user_major')
            user_enroll = request.session.get('user_enroll')
            user_profile = request.session.get('user_profile')

            
            user = User.objects.create_user(
                username=request.POST['user_id'],
                password=request.POST['user_pw']                
                )
            
            profile = Profile(
                user=user,
                user_name=user_name,
                user_phone=user_phone,
                user_birth=user_birth,
                user_major=user_major,
                user_enroll=user_enroll,
                user_profile=user_profile
            )
            profile.save()

            auth.login(request, user)
            return redirect('main:mainpage')

    return render(request, 'accounts/signup3.html')

def finish_signup(request):
    return render(request, 'accounts/finish-signup.html')

# def signup(request):
#     if request.method == 'POST':
#         user_id = request.POST.get('user_id')
#         user_pw = request.POST.get('user_pw')
#         if request.POST['user_pw'] == request.POST['confirm']:
#                 if User.objects.filter(username=user_id).exists():
#                     return render(request, 'accounts/signup.html', {'error': 'Username already exists'})
#                 user = User.objects.create_user(
#                     username=request.POST['user_id'],
#                     password=request.POST['user_pw']
#                 )
#                 user_name = request.POST['user_name']
#                 user_phone = request.POST['user_phone']
#                 user_birth = request.POST['user_birth']
#                 user_enroll = request.POST['user_enroll']
                
    
                
#                 profile = Profile(user=user,
#                                 user_name=user_name,
#                                 user_phone=user_phone,
#                                 user_birth=user_birth,
#                                 user_enroll=user_enroll
#                                 )
#                 profile.save()

#                 auth.login(request, user)
#                 return redirect('main:mainpage')
        
#     return render(request, 'accounts/signup.html')

