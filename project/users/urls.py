from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path('mypage/<int:id>/', mypage, name="mypage"),
    path('edit_portfolio/', edit_portfolio, name='edit_portfolio'),
    path('follow-list/<int:id>', follow_list, name="follow-list"),
    path('bookmark/<int:id>', bookmark, name="bookmark"),
<<<<<<< HEAD
    path('update-profile/<int:id>', update_profile, name="update-profile"),
=======
>>>>>>> 8f385948905ccdfdc940f2b55f5cccba573b3795
    path('my-writing/<int:id>', my_writing, name="my-writing"),
    path('mentoring/<int:id>', mentoring, name="mentoring"),
    path('career-now/<int:id>', career_now, name="career-now")
]