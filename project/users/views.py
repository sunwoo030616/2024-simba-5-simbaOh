from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

# Create your views here.
def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    context = {
        'target_user':user
    }
    return render(request, 'users/mypage.html', context)