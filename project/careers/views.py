from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Careerinfo, Careerinfotag, Careerprogram, Careerprogramtag, Eduinfo, Eduinfotag

def career_info(request):
    order = request.GET.get('order', 'latest')
    
    if order == 'latest':
        careerinfos = Careerinfo.objects.all().order_by('-pub_date')
    elif order == 'oldest':
        careerinfos = Careerinfo.objects.all().order_by('pub_date')
    else:
        careerinfos = Careerinfo.objects.all()
    total_careerinfo_count = careerinfos.count()
    return render(request, 'careers/career-info.html', {
        'careerinfos': careerinfos,
        'total_careerinfo_count': total_careerinfo_count,
        'selected_order': order
    })

def career_program(request):
    order = request.GET.get('order', 'latest')
    
    if order == 'latest':
        careerprograms = Careerprogram.objects.all().order_by('-pub_date')
    elif order == 'oldest':
        careerprograms = Careerprogram.objects.all().order_by('pub_date')
    else:
        careerprograms = Careerprogram.objects.all()
    total_careerprogram_count = careerprograms.count()
    return render(request, 'careers/career-program.html', {
        'careerprograms': careerprograms,
        'total_careerprogram_count': total_careerprogram_count,
        'selected_order': order
    })

def edu_info(request):
    order = request.GET.get('order', 'latest')
    
    if order == 'latest':
        eduinfos = Eduinfo.objects.all().order_by('-pub_date')
    elif order == 'oldest':
        eduinfos = Eduinfo.objects.all().order_by('pub_date')
    else:
        eduinfos = Eduinfo.objects.all()
    total_eduinfo_count = eduinfos.count()
    return render(request, 'careers/edu-info.html', {
        'eduinfos': eduinfos,
        'total_eduinfo_count': total_eduinfo_count,
        'selected_order': order
    })

def careerinfo_create(request):
    new_careerinfo = Careerinfo()

    new_careerinfo.title = request.POST['title']
    new_careerinfo.writer = request.user
    new_careerinfo.company = request.POST['company']
    new_careerinfo.field = request.POST['field']
    new_careerinfo.content = request.POST['content']
    new_careerinfo.startline = request.POST['startline']
    new_careerinfo.deadline = request.POST['deadline']
    new_careerinfo.pub_date = timezone.now()
    new_careerinfo.image = request.FILES.get('image')

    new_careerinfo.save()

    words = new_careerinfo.content.split(' ')
    careerinfotag_list = []
    for w in words:
        if len(w)>0:
            if w[0] == '#':
                careerinfotag_list.append(w[1:])
    
    for t in careerinfotag_list:
        careerinfotag, boolean = Careerinfotag.objects.get_or_create(name=t)
        new_careerinfo.careerinfotags.add(careerinfotag.id)
    return redirect('careers:careerinfo-detail', new_careerinfo.id)

def careerprogram_create(request):
    new_careerprogram = Careerprogram()

    new_careerprogram.title = request.POST['title']
    new_careerprogram.writer = request.user
    new_careerprogram.field = request.POST['field']
    new_careerprogram.place = request.POST['place']
    new_careerprogram.content = request.POST['content']
    new_careerprogram.startline = request.POST['startline'] 
    new_careerprogram.deadline = request.POST['deadline']
    new_careerprogram.pub_date = timezone.now()
    new_careerprogram.image = request.FILES.get('image')

    new_careerprogram.save()

    words = new_careerprogram.content.split(' ')
    careerprogramtag_list = []
    for w in words:
        if len(w)>0:
            if w[0] == '#':
                careerprogramtag_list.append(w[1:])
    
    for t in careerprogramtag_list:
        careerprogramtag, boolean = Careerprogramtag.objects.get_or_create(name=t)
        new_careerprogram.careerprogramtags.add(careerprogramtag.id)
    return redirect('careers:careerprogram-detail', new_careerprogram.id)

def eduinfo_create(request):
    new_eduinfo = Eduinfo()

    new_eduinfo.title = request.POST['title']
    new_eduinfo.writer = request.user
    new_eduinfo.place = request.POST['place']
    new_eduinfo.field = request.POST['field']
    new_eduinfo.content = request.POST['content']
    new_eduinfo.startline = request.POST['startline']
    new_eduinfo.deadline = request.POST['deadline']
    new_eduinfo.pub_date = timezone.now()
    new_eduinfo.image = request.FILES.get('image')

    new_eduinfo.save()

    words = new_eduinfo.content.split(' ')
    eduinfotag_list = []
    for w in words:
        if len(w)>0:
            if w[0] == '#':
                eduinfotag_list.append(w[1:])
    
    for t in eduinfotag_list:
        eduinfotag, boolean = eduinfotag.objects.get_or_create(name=t)
        new_eduinfo.eduinfotags.add(eduinfotag.id)
    return redirect('careers:eduinfo-detail', new_eduinfo.id)

def new_careerinfo(request):
    return render(request, 'careers/new-careerinfo.html')

def new_careerprogram(request):
    return render(request, 'careers/new-careerprogram.html')

def careerinfo_detail(request, id):
    careerinfo = get_object_or_404(Careerinfo, pk=id)
    return render(request, 'careers/careerinfo-detail.html', {'careerinfo': careerinfo})

def careerprogram_detail(request, id):
    careerprogram = get_object_or_404(Careerprogram, pk=id)
    return render(request, 'careers/careerprogram-detail.html', {'careerprogram': careerprogram})



def careerinfo_delete(request, id):
    delete_careerinfo = Careerinfo.objects.get(pk=id)
    delete_careerinfo.delete()
    return redirect('careers:career-info')

def careerprogram_delete(request, id):
    delete_careerprogram_ = Careerprogram.objects.get(pk=id)
    delete_careerprogram_.delete()
    return redirect('careers:career-program')

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



