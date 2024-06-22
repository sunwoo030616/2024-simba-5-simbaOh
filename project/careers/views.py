from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Careerinfo, Careerinfotag, Careerprogram, Careerprogramtag

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



def new_careerinfo(request):
    return render(request, 'careers/new-careerinfo.html')

def new_careerprogram(request):
    return render(request, 'careers/new-careerprogram.html')

def careerinfo_detail(request, id):
    careerinfo = get_object_or_404(Careerinfo, pk=id)
    return render(request, 'careers/careerinfo-detail.html', {'careerinfo': careerinfo})

def careerinfo_delete(request, id):
    delete_careerinfo = Careerinfo.objects.get(pk=id)
    delete_careerinfo.delete()
    return redirect('careers:career-info')

def careerinfotag_careerinfos(request, careerinfotag_id):
    careerinfotag = get_object_or_404(Careerinfotag, id=careerinfotag_id)
    careerinfos = careerinfotag.careerinfos.all()
    return render(request, 'careers/careerinfotag-careerinfo.html', {
        'careerinfotag' : careerinfotag,
        'careerinfos' : careerinfos
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



