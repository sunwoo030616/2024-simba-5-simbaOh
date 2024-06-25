from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Portfolio, Education, Experience, Project, Certification
from accounts.models import Profile
from main.models import Mentor, Relation_mentor, Menti
from community.models import Free, Move
from careers.models import Careerinfo, Careerprogram, Eduinfo, Ciapply, Cpapply, Eiapply

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
        'followings': user.mentor_followings.all(),
        'followers': user.profile.followers.all()
    }
    return render(request, 'users/follow_list.html', context)

def bookmark(request, id):
    return render(request, 'users/bookmark.html')

def ciapply(request):
    ci_apply=Ciapply.objects.filter(user=request.user)
    return render(request, 'users/ciapply.html', {'ci_apply': ci_apply})

def cpapply(request):
    cp_apply=Cpapply.objects.filter(user=request.user)
    return render(request, 'users/cpapply.html', {'cp_apply': cp_apply})

def eiapply(request):
    ei_apply=Eiapply.objects.filter(user=request.user)
    return render(request, 'users/eiapply.html', {'ei_apply': ei_apply})

def edit_portfolio(request):
    portfolio, created = Portfolio.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title', '')
        introduction = request.POST.get('introduction', '')
        education_list = request.POST.getlist('education', [])
        experience_list = request.POST.getlist('experience', [])
        projects_list = request.POST.getlist('projects', [])
        certifications_list = request.POST.getlist('certifications', [])

        portfolio.title = title
        portfolio.introduction = introduction

        portfolio.education.clear()
        for edu in education_list:
            if edu:  # 비어 있지 않은지 확인
                education, created = Education.objects.get_or_create(name=edu)
                portfolio.education.add(education)

        portfolio.experience.clear()
        for exp in experience_list:
            if exp:  # 비어 있지 않은지 확인
                experience, created = Experience.objects.get_or_create(name=exp)
                portfolio.experience.add(experience)

        portfolio.projects.clear()
        for proj in projects_list:
            if proj:  # 비어 있지 않은지 확인
                project, created = Project.objects.get_or_create(name=proj)
                portfolio.projects.add(project)

        portfolio.certifications.clear()
        for cert in certifications_list:
            if cert:  # 비어 있지 않고 문자열인지 확인
                certification, created = Certification.objects.get_or_create(name=cert)
                portfolio.certifications.add(certification)

        portfolio.save()

        # 디버깅을 위해 저장된 데이터를 출력합니다.
        print('Title:', portfolio.title)
        print('Introduction:', portfolio.introduction)
        print('Education:', [edu.name for edu in portfolio.education.all()])
        print('Experience:', [exp.name for exp in portfolio.experience.all()])
        print('Projects:', [proj.name for proj in portfolio.projects.all()])
        print('Certifications:', [cert.name for cert in portfolio.certifications.all()])

        return redirect('users:portfolio', id=request.user.id)

    return render(request, 'users/edit_portfolio.html', {'portfolio': portfolio})

def view_portfolio(request, id):
    user = get_object_or_404(User, pk=id)
    portfolio, created = Portfolio.objects.get_or_create(user=user)
    portfolio = get_object_or_404(Portfolio, user=user)
    education = portfolio.education.all()
    experience = portfolio.experience.all()
    projects = portfolio.projects.all()
    certifications = portfolio.certifications.all()
    return render(request, 'users/portfolio.html', {
        'portfolio': portfolio,
        'education': education,
        'experience': experience,
        'projects': projects,
        'certifications': certifications
    })

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
    user = get_object_or_404(User, pk=id)
    # mentor_state = Relation_mentor.objects.filter(menti=user)
    mentor = Menti.objects.filter(user=user)
    mentor_state = Relation_mentor.objects.filter(menti=user)
    context = {
        # 'menti_ship': user.menti_ship.all(),
        # 'mentor_state':mentor_state.all(),
        'mentor':mentor.all(),
    }
    return render(request, 'users/mentoring.html', context)

def menti_list(request, id):
    user = get_object_or_404(User, pk=id)
    mentors = Mentor.objects.all()
    mentor = Menti.objects.filter(user=user)
    # mentors = Mentor.objects.filter(user_id=id)
    menti = []
    for mentor in mentors:
        if mentor.user_id == id:
            m = Menti.objects.filter(mentor=mentor)
            menti.extend(m)

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> e6715bb8a3d97fa9f231635d3a6f7aa7006eeede
>>>>>>> ead2896594494d561fa1a81e29a42a25d160586a
    return render(request, 'users/menti_list.html', {
        'menti':menti,
        'mentor':mentor
        })
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
    return render(request, 'users/menti_list.html', {'menti':menti})
>>>>>>> f451066de61bfdf716ae119adefdae24d64b51b7
>>>>>>> e6715bb8a3d97fa9f231635d3a6f7aa7006eeede
>>>>>>> ead2896594494d561fa1a81e29a42a25d160586a


def mentoring_state(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        mentorship_id = request.POST.get('mentorship_id')
        state = request.POST.get('state')
        try:
            mentoring = Menti.objects.get(pk=mentorship_id)
            if state == '거절':
                mentoring.state = "거절"
            elif state == '수락':
                mentoring.state = '수락'
            else:
                mentoring.state = '대기'
            mentoring.save()  # Save the state change
        except Relation_mentor.DoesNotExist:
            # Handle the case where the mentorship does not exist
            pass
    return redirect('users:mentoring', user.id)

def career_now(request, id):
    return render(request, 'users/career_now.html')



def cibm_list(request):
    user = request.user
    cibms = user.ci_bms.all()
    return render(request, 'users/cibm.html', {'cibms': cibms})

def cpbm_list(request):
    user = request.user
    cpbms = user.cp_bms.all()
    return render(request, 'users/cpbm.html', {'cpbms': cpbms})

def eibm_list(request):
    user = request.user
    eibms = user.ei_bms.all()
    return render(request, 'users/eibm.html', {'eibms': eibms})

def ci_bms(request, careerinfo_id):
    careerinfo = get_object_or_404(Careerinfo, id=careerinfo_id)
    if request.user in careerinfo.ci_bm.all():
        careerinfo.ci_bm.remove(request.user)
        careerinfo.cibm_count-=1
        careerinfo.save()
    else:
        careerinfo.ci_bm.add(request.user)
        careerinfo.cibm_count +=1
        careerinfo.save()
    return redirect('users:cibm_list')

def cp_bms(request, careerprogram_id):
    careerprogram = get_object_or_404(Careerprogram, id=careerprogram_id)
    if request.user in careerprogram.cp_bm.all():
        careerprogram.cp_bm.remove(request.user)
        careerprogram.cpbm_count-=1
        careerprogram.save()
    else:
        careerprogram.cp_bm.add(request.user)
        careerprogram.cpbm_count +=1
        careerprogram.save()
    return redirect('users:cpbm_list')

def ei_bms(request, eduinfo_id):
    eduinfo = get_object_or_404(Eduinfo, id=eduinfo_id)
    if request.user in eduinfo.ei_bm.all():
        eduinfo.ei_bm.remove(request.user)
        eduinfo.eibm_count-=1
        eduinfo.save()
    else:
        eduinfo.ei_bm.add(request.user)
        eduinfo.eibm_count +=1
        eduinfo.save()
    return redirect('users:eibm_list') 

