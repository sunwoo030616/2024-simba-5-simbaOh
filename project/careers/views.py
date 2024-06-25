from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q
from .models import Careerinfo, Careerinfotag, Careerprogram, Careerprogramtag, Eduinfo, Eduinfotag, Ciapply, Cpapply, Eiapply
from django.db.models import Sum
def career_info(request):
    order = request.GET.get('order', 'latest')
    search_query = request.GET.get('search', '')
    if search_query.startswith('#'):
        tag_name = search_query[1:]
        careerinfos = Careerinfo.objects.filter(
            Q(careerinfotags__name__icontains=tag_name)
        ).distinct()
    else:
        careerinfos = Careerinfo.objects.filter(
            Q(title__icontains=search_query) |
            Q(company__icontains=search_query) |
            Q(field__icontains=search_query) |
            Q(content__icontains=search_query)
        ).distinct()

    if order == 'latest':
        careerinfos = careerinfos.order_by('-pub_date')
    elif order == 'oldest':
        careerinfos = careerinfos.order_by('pub_date')

    total_careerinfo_count = careerinfos.count()
    return render(request, 'careers/career-info.html', {
        'careerinfos': careerinfos,
        'total_careerinfo_count': total_careerinfo_count,
        'selected_order': order,
        'search_query': search_query,
    })

def career_program(request):
    order = request.GET.get('order', 'latest')
    search_query = request.GET.get('search', '')
    if search_query.startswith('#'):
        tag_name = search_query[1:]
        careerprograms = Careerprogram.objects.filter(
            Q(careerprogramtags__name__icontains=tag_name)
        ).distinct()
    else:
        careerprograms = Careerprogram.objects.filter(
            Q(title__icontains=search_query) |
            Q(place__icontains=search_query) |
            Q(field__icontains=search_query) |
            Q(content__icontains=search_query)
        ).distinct()

    if order == 'latest':
        careerprograms = careerprograms.order_by('-pub_date')
    elif order == 'oldest':
        careerprograms = careerprograms.order_by('pub_date')

    total_careerprogram_count = careerprograms.count()
    return render(request, 'careers/career-program.html', {
        'careerprograms': careerprograms,
        'total_careerprogram_count': total_careerprogram_count,
        'selected_order': order,
        'search_query': search_query,
    })

def edu_info(request):
    order = request.GET.get('order', 'latest')
    search_query = request.GET.get('search', '')
    if search_query.startswith('#'):
        tag_name = search_query[1:]
        eduinfos = Eduinfo.objects.filter(
            Q(eduinfotags__name__icontains=tag_name)
        ).distinct()
    else:
        eduinfos = Eduinfo.objects.filter(
            Q(title__icontains=search_query) |
            Q(place__icontains=search_query) |
            Q(field__icontains=search_query) |
            Q(content__icontains=search_query)
        ).distinct()

    if order == 'latest':
        eduinfos = eduinfos.order_by('-pub_date')
    elif order == 'oldest':
        eduinfos = eduinfos.order_by('pub_date')

    total_eduinfo_count = eduinfos.count()
    return render(request, 'careers/edu-info.html', {
        'eduinfos': eduinfos,
        'total_eduinfo_count': total_eduinfo_count,
        'selected_order': order,
        'search_query': search_query,
    })

def careerinfo_create(request):
    if request.method == "POST":
        # 디버그 출력문 추가
        print(request.POST)

        new_careerinfo = Careerinfo()

        new_careerinfo.title = request.POST.get('title')
        new_careerinfo.writer = request.user
        new_careerinfo.company = request.POST.get('company')
        new_careerinfo.field = request.POST.get('field')
        new_careerinfo.content = request.POST.get('content')
        new_careerinfo.startline = request.POST.get('startline')
        new_careerinfo.deadline = request.POST.get('deadline')
        new_careerinfo.pub_date = timezone.now()
        new_careerinfo.image = request.FILES.get('image')
        
        new_careerinfo.save()

        careerinfotags = request.POST.get('careerinfotags', '')
        tag_names = [tag.strip() for tag in careerinfotags.split('#') if tag.strip()]
        
        careerinfotag_list = []
        for tag_name in tag_names:
            careerinfotag, created = Careerinfotag.objects.get_or_create(name=tag_name)
            careerinfotag_list.append(careerinfotag)

        new_careerinfo.careerinfotags.set(careerinfotag_list)

        return redirect('careers:careerinfo-detail', new_careerinfo.id)

    return render(request, 'careers/new-careerinfo.html')

def careerprogram_create(request):
    if request.method == "POST":
        # 디버그 출력문 추가
        print(request.POST)

        new_careerprogram = Careerprogram()

        new_careerprogram.title = request.POST.get('title')
        new_careerprogram.writer = request.user
        new_careerprogram.place = request.POST.get('place')
        new_careerprogram.field = request.POST.get('field')
        new_careerprogram.content = request.POST.get('content')
        new_careerprogram.startline = request.POST.get('startline')
        new_careerprogram.deadline = request.POST.get('deadline')
        new_careerprogram.pub_date = timezone.now()
        new_careerprogram.image = request.FILES.get('image')
        
        new_careerprogram.save()

        careerprogramtags = request.POST.get('careerprogramtags', '')
        tag_names = [tag.strip() for tag in careerprogramtags.split('#') if tag.strip()]
        
        careerprogramtag_list = []
        for tag_name in tag_names:
            careerprogramtag, created = careerprogramtag.objects.get_or_create(name=tag_name)
            careerprogramtag_list.append(careerprogramtag)

        new_careerprogram.careerprogramtags.set(careerprogramtag_list)

        return redirect('careers:careerprogram-detail', new_careerprogram.id)

    return render(request, 'careers/new-careerprogram.html')

def eduinfo_create(request):
    if request.method == "POST":
        new_eduinfo = Eduinfo()
        
        new_eduinfo.title = request.POST.get('title')
        new_eduinfo.writer = request.user
        new_eduinfo.place = request.POST.get('place')
        new_eduinfo.field = request.POST.get('field')
        new_eduinfo.content = request.POST.get('content')
        new_eduinfo.startline = request.POST.get('startline')
        new_eduinfo.deadline = request.POST.get('deadline')
        new_eduinfo.pub_date = timezone.now()
        new_eduinfo.image = request.FILES.get('image')
        
        new_eduinfo.save()

        eduinfotags = request.POST.get('eduinfotags', '')
        tag_names = [tag.strip() for tag in eduinfotags.split('#') if tag.strip()]
        
        eduinfotag_list = []
        for tag_name in tag_names:
            eduinfotag, created = Eduinfotag.objects.get_or_create(name=tag_name)
            eduinfotag_list.append(eduinfotag)

        new_eduinfo.eduinfotags.set(eduinfotag_list)

        return redirect('careers:eduinfo-detail', new_eduinfo.id)

    return render(request, 'careers/new-eduinfo.html')


def new_careerinfo(request):
    return render(request, 'careers/new-careerinfo.html')

def new_careerprogram(request):
    return render(request, 'careers/new-careerprogram.html')

def new_eduinfo(request):
    return render(request, 'careers/new-eduinfo.html')

def careerinfo_detail(request, id):
    careerinfo = get_object_or_404(Careerinfo, pk=id)
    user = request.user
    has_applied = Ciapply.objects.filter(user=user, careerinfo=careerinfo).exists()
    return render(request, 'careers/careerinfo-detail.html', {
        'careerinfo': careerinfo,
        'has_applied': has_applied
    })

def careerprogram_detail(request, id):
    careerprogram = get_object_or_404(Careerprogram, pk=id)
    user = request.user
    has_applied = Cpapply.objects.filter(user=user, careerprogram=careerprogram).exists()
    return render(request, 'careers/careerprogram-detail.html', {
        'careerprogram': careerprogram,
        'has_applied': has_applied
    })

def eduinfo_detail(request, id):
    eduinfo = get_object_or_404(Eduinfo, pk=id)
    user = request.user
    has_applied = Eiapply.objects.filter(user=user, eduinfo=eduinfo).exists()
    return render(request, 'careers/eduinfo-detail.html', {
        'eduinfo': eduinfo,
        'has_applied': has_applied
    })


def careerinfo_delete(request, id):
    delete_careerinfo = Careerinfo.objects.get(pk=id)
    delete_careerinfo.delete()
    return redirect('careers:career-info')

def careerprogram_delete(request, id):
    delete_careerprogram_ = Careerprogram.objects.get(pk=id)
    delete_careerprogram_.delete()
    return redirect('careers:career-program')

def eduinfo_delete(request, id):
    delete_eduinfo = Eduinfo.objects.get(pk=id)
    delete_eduinfo.delete()
    return redirect('careers:edu-info')

def careerinfotag_careerinfos(request, careerinfotag_id):
    careerinfotag = get_object_or_404(Careerinfotag, id=careerinfotag_id)
    careerinfos = careerinfotag.careerinfos.all()
    return render(request, 'careers/careerinfotag-careerinfo.html', {
        'careerinfotag' : careerinfotag,
        'careerinfos' : careerinfos
    })

def careerprogramtag_careerprograms(request, careerprogramtag_id):
    careerprogramtag = get_object_or_404(Careerprogramtag, id=careerprogramtag_id)
    careerprograms = careerprogramtag.careerprograms.all()
    return render(request, 'careers/careerprogramtag-careerprogram.html', {
        'careerprogramtag' : careerprogramtag,
        'careerprograms' : careerprograms
    })

def eduinfotag_eduinfos(request, eduinfotag_id):
    eduinfotag = get_object_or_404(Eduinfotag, id=eduinfotag_id)
    eduinfos = eduinfotag.eduinfos.all()
    return render(request, 'careers/eduinfotag-eduinfo.html', {
        'eduinfotag' : eduinfotag,
        'eduinfos' : eduinfos
    })

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
    return redirect('careers:careerinfo-detail', careerinfo.id)

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
    return redirect('careers:careerprogram-detail', careerprogram.id)

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
    return redirect('careers:eduinfo-detail', eduinfo.id)

def apply_careerinfo(request, id):
    careerinfo = get_object_or_404(Careerinfo, pk=id)
    if request.method == 'POST':
        user = request.user
    # 이미 지원했는지 확인
        existing_application = Ciapply.objects.filter(user=user, careerinfo=careerinfo).first()
        if existing_application:
        # 이미 지원했다면 지원 취소
            existing_application.delete()
        else:
        # 지원하지 않았다면 새로 지원
            Ciapply.objects.create(user=user, careerinfo=careerinfo)
    
        return redirect('users:ciapply')

    return redirect('careers:careerinfo-detail', id=id)

def apply_careerprogram(request, id):
    careerprogram = get_object_or_404(Careerprogram, pk=id)
    if request.method == 'POST':
        user = request.user
    # 이미 지원했는지 확인
        existing_application = Cpapply.objects.filter(user=user, careerprogram=careerprogram).first()
        if existing_application:
        # 이미 지원했다면 지원 취소
            existing_application.delete()
        else:
        # 지원하지 않았다면 새로 지원
            Cpapply.objects.create(user=user, careerprogram=careerprogram)
    
        return redirect('users:cpapply')

    return redirect('careers:careerprogram-detail', id=id)

def apply_eduinfo(request, id):
    eduinfo = get_object_or_404(Eduinfo, pk=id)
    if request.method == 'POST':
        user = request.user
    # 이미 지원했는지 확인
        existing_application = Eiapply.objects.filter(user=user, eduinfo=eduinfo).first()
        if existing_application:
        # 이미 지원했다면 지원 취소
            existing_application.delete()
        else:
        # 지원하지 않았다면 새로 지원
            Eiapply.objects.create(user=user, eduinfo=eduinfo)
    
        return redirect('users:eiapply')
    
