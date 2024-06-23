from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path('mypage/<int:id>/', mypage, name="mypage"),
    path('edit_portfolio/', edit_portfolio, name='edit_portfolio'),
    path('follow-list/<int:id>', follow_list, name="follow-list"),
    path('bookmark/<int:id>', bookmark, name="bookmark"),
    path('my-writing/<int:id>', my_writing, name="my-writing"),
    path('mentoring/<int:id>', mentoring, name="mentoring"),
    path('career-now/<int:id>', career_now, name="career-now"),
    path('menti-list/<int:id>/', menti_list, name="menti-list"),
    path('cibms/', cibm_list, name="cibm_list"),
    path('cpbms/', cpbm_list, name="cpbm_list"),
    path('eibms/', eibm_list, name="eibm_list"),
    path('ciapply/', ciapply, name="ciapply"),
    path('cpapply/', cpapply, name="cpapply"),
    path('eiapply/', eiapply, name="eiapply"),
]