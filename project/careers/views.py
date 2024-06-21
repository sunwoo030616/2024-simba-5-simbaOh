from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Careerinfo

def career_info(request):
    careerinfos = Careerinfo.objects.all()
    return render(request, 'careers/career-info.html', {'careerinfos': careerinfos})

def careerinfo_create(request):
    new_careerinfo = Careerinfo()

    new_careerinfo.title = request.POST['title']
    new_careerinfo.company = request.POST['company']
    new_careerinfo.place = request.POST['place']
    new_careerinfo.content = request.POST['content']
    new_careerinfo.deadline = request.POST['deadline']
    new_careerinfo.pub_date = timezone.now()
    new_careerinfo.image = request.FILES.get('image')

    new_careerinfo.save()

    return redirect('careers:careerinfo-detail', new_careerinfo.id)

def new_careerinfo(request):
    return render(request, 'careers/new-careerinfo.html')

def careerinfo_detail(request, id):
    careerinfo = get_object_or_404(Careerinfo, pk=id)
    return render(request, 'careers/careerinfo-detail.html', {'careerinfo': careerinfo})

def careerinfo_delete(request, id):
    delete_careerinfo = Careerinfo.objects.get(pk=id)
    delete_careerinfo.delete()
    return redirect('careers:career-info')