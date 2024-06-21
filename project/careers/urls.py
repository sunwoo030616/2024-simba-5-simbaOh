from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views
from .views import *

app_name = "careers"

urlpatterns = [
    path('career-info/', career_info, name="career-info"),
    path('new-careerinfo/', new_careerinfo, name="new-careerinfo"),
    path('careerinfo-create/', careerinfo_create, name="careerinfo-create"),
    path('careerinfo-detail/<int:id>/', careerinfo_detail, name="careerinfo-detail"),
    path('careerinfo-delete/<int:id>/', careerinfo_delete, name="careerinfo-delete"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)