from django.contrib import admin
from django.urls import path
from main import views
from .views import *

app_name = "careers"

urlpatterns = [
<<<<<<< HEAD
    path('new-info/', new_info, name="new-info"),
    path('create/', create, name="create"),
    path('career-info/', career_info, name="career-info"),
    path('detail/<int:id>/', detail, name="detail"),
    path('edit/<int:id>/', edit, name="edit"),
    path('delete/<int:id>/', delete, name="delete"),
=======
    path('new-info', new_info, name="new-info"),
    path('create', create, name="create"),
    path('career-info', career_info, name="career-info"),
    path('detail/<int:id>', detail, name="detail"),
    path('edit/<int:id>', edit, name="edit"),
    path('delete/<int:id>', delete, name="delete"),
>>>>>>> f2d5fc7f8f4219678cdbb76036679360a2a7dcb1
]