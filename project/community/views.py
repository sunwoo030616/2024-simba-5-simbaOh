from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Community
# Create your views here.

def communities(request):
    posts = Community.objects.all()
    return render(request, 'community/communities.html', {'posts': posts})

def new_post(request):
    return render(request, 'community/new-post.html')

def detailc(request, id):
    post = get_object_or_404(Community, pk=id)
    return render(request, 'community/detailc.html', {'post':post})

def editc(request, id):
    edit_post = Community.objects.get(pk=id)
    return render(request, 'community/editc.html', {'post' : edit_post})

def create(request):
    if request.method == 'POST':
        new_post = Community()
        new_post.title = request.POST.get('title', '')
        new_post.writer = request.user
        new_post.body = request.POST.get('body', '')
        new_post.pub_date = timezone.now()
        new_post.save()
        return redirect('community:detailc', new_post.id)
    return render(request, 'community/new-post.html')

def update(request, id):
    update_post = Community.objects.get(pk=id)

    update_post.title = request.POST['title']
    update_post.body = request.POST['body']
    update_post.pub_date = timezone.now()

    update_post.save()

    return redirect('community:detailc', update_post.id)

def delete(request, id):
    delete_post = Community.objects.get(pk=id)
    delete_post.delete()
    return redirect('community:communities')