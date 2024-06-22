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
    path('careerinfotag-careerinfos/<int:careerinfotag_id>/', careerinfotag_careerinfos, name="careerinfotag-careerinfos"),
    path('ci_bms/<int:careerinfo_id>', ci_bms, name="ci_bms"),
    path('career-program/', career_program, name="career-program"),
    path('new-careerprogram/', new_careerprogram, name="new-careerprogram"),
    path('careerprogram-create/', careerprogram_create, name="careerprogram-create"),
    path('careerprogram-detail/<int:id>/', careerprogram_detail, name="careerprogram-detail"),
    path('careerprogram-delete/<int:id>/', careerprogram_delete, name="careerprogram-delete"),
    path('careerprogramtag-careerprograms/<int:careerprogramtag_id>/', careerprogramtag_careerprograms, name="careerprogramtag-careerprograms"),
    path('cp_bms/<int:careerprogram_id>', cp_bms, name="cp_bms"),
    path('edu-info/', edu_info, name="edu-info"),
    path('new-eduinfo/', new_eduinfo, name="new-eduinfo"),
    path('eduinfo-create/', eduinfo_create, name="eduinfo-create"),
    path('eduinfo-detail/<int:id>/', eduinfo_detail, name="eduinfo-detail"),
    path('eduinfo-delete/<int:id>/', eduinfo_delete, name="eduinfo-delete"),
    path('eduinfotag-eduinfos/<int:eduinfotag_id>/', eduinfotag_eduinfos, name="eduinfotag-eduinfos"),
    path('ei_bms/<int:eduinfo_id>', ei_bms, name="ei_bms"),
    path('careerinfo-detail/<int:id>/apply/', apply_careerinfo, name="apply_careerinfo"),
    path('careerprogram-detail/<int:id>/apply/', apply_careerprogram, name="apply_careerprogram"),
    path('eduinfo-detail/<int:id>/apply/', apply_eduinfo, name="apply_eduinfo"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)