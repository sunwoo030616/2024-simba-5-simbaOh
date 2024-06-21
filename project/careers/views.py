from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Info

# Create your views here.
def new_info(request):
    return render(request, 'careers/new-info.html')

def career_info(request):
    infos = Info.objects.all()
    return render(request, 'careers/career-info.html', {'infos': infos})

def detail(request, id):
    info = get_object_or_404(Info, pk=id)
    return render(request, 'careers/detail.html', {'info' : info})

def edit(request, id):
    edit_info = get_object_or_404(Info, pk=id)
    return render(request, 'careers/edit.html', {'info' : edit_info})

def create(request):
    new_info = Info()

    new_info.title = request.POST['title']
    new_info.writer = request.POST['writer']
    new_info.location = request.POST['location']
    new_info.pub_date=timezone.now()

    new_info.save()

    return redirect('careers:detail', new_info.id)

def delete(request, id):
    delete_info = Info.objects.get(pk=id)
    delete_info.delete()
    return redirect('careers:career-info')