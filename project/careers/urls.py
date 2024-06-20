from django.contrib import admin
from django.urls import path
from main import views
from .views import *

app_name = "careers"

urlpatterns = [
    path('new-info/', new_info, name="new-info"),
    path('create/', create, name="create"),
    path('career-info/', career_info, name="career-info"),
    path('detail/<int:id>/', detail, name="detail"),
    path('edit/<int:id>/', edit, name="edit"),
    path('delete/<int:id>/', delete, name="delete"),
]