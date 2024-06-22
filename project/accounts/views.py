from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from .models import Profile, Request

# 로그인 뷰
def login(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']

        user = auth.authenticate(request, username=user_id, password=user_pw)

        if user is not None:
            auth.login(request, user)
            return redirect('main:mainpage')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')

# 로그아웃 뷰
def logout(request):
    auth.logout(request)
    return redirect('main:first_screen')

# 회원가입 뷰 (1단계)
def signup(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']

        if request.POST['user_pw'] == request.POST['confirm']:
            if User.objects.filter(username=user_id).exists():
                return render(request, 'accounts/signup.html', {'error': 'Username already exists'})

            user = User.objects.create_user(
                username=user_id,
                password=user_pw
            )

            # Profile 객체가 없을 경우에만 생성
            if not hasattr(user, 'profile'):
                Profile.objects.create(
                    user=user,
                    user_name='',
                    user_phone='',
                    user_birth='2000-01-01',  # 기본값으로 임시 설정
                    user_major='',
                    user_enroll='',
                    user_profile=None
                )
                Request.objects.create(
                    menti_ship = ''
                )


            request.session['user_id'] = user.id
            request.session.modified = True  # Ensure session is saved

            return redirect('accounts:signup2')
    return render(request, 'accounts/signup.html')

# 회원가입 뷰 (2단계)
def signup2(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        user_major = request.POST['user_major']
        user_enroll = request.POST['user_enroll']
        user_profile = request.FILES.get('user_profile')

        if user_id:
            user = User.objects.get(id=user_id)
            user.profile.user_major = user_major
            user.profile.user_enroll = user_enroll
            if user_profile:
                user_profile_path = default_storage.save(f'images/{user_profile.name}', user_profile)
                user.profile.user_profile = user_profile_path
            user.profile.save()

            request.session.modified = True  # Ensure session is saved

            return redirect('accounts:signup3')
    return render(request, 'accounts/signup2.html')

# 회원가입 뱁 (3단계)
def signup3(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        user_name = request.POST['user_name']
        user_phone = request.POST['user_phone']
        user_birth = request.POST['user_birth']

        if user_id:
            user = User.objects.get(id=user_id)
            user.profile.user_name = user_name
            user.profile.user_phone = user_phone
            user.profile.user_birth = user_birth
            user.profile.save()

            auth.login(request, user)
            return redirect('accounts:finishjoin')
    return render(request, 'accounts/signup3.html')

def update_profile(request, id):
    update_profile = Profile.objects.get(pk=id)

    if request.user.is_authenticated and request.user == update_profile.user:
        if request.method == 'POST':
            update_profile.user_name = request.POST.get('user_name')
            update_profile.user_phone = request.POST.get('user_phone')
            update_profile.user_major = request.POST.get('user_major')
            update_profile.user_enroll = request.POST.get('user_enroll')
            
            if request.FILES.get('user_profile'):
                update_profile.user_profile = request.FILES.get('user_profile')
            
            update_profile.save()

            return redirect('main:mainpage')
        else:
            return render(request, 'accounts/update_profile.html', {'profile': update_profile})
    return redirect('accounts:login')

def finishjoin(request):
    return render(request, 'accounts/finishjoin.html')
