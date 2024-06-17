from django.shortcuts import render, redirect, get_object_or_404
from .models import Mentor

<<<<<<< HEAD
# Create your views here.
=======
# Create your views here.
def mainpage(request):
    return render(request, 'main/mainpage.html')

def mentor_start(request):
    return render(request, 'main/mentor_start.html')

def mentor_list(request):
    mentors = Mentor.objects.all()
    return render(request, 'mentor_list.html', {'mentors' : mentors})

def mentor_info(request, id):
    mentor = get_object_or_404(Mentor, pk = id)
    return render(request, 'mentor_info.html', {'mentor' : mentor})
>>>>>>> 5a339e109c3e3b7d69ba9b0de2bf5abe13bab1a9
