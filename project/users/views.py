from django.shortcuts import render, get_object_or_404
from .models import User

def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request, 'users/mypage.html', {'user': user})
