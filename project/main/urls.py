from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "main"
urlpatterns = [
    path('', intro, name='intro'),
    path('first-screen', first_screen, name='first-screen'),
    path('mainpage', mainpage, name='mainpage'),
    path('mentor-start', mentor_start, name='mentor-start'),
    path('mentor-list/', mentor_list, name='mentor-list'),
    path('mentor-info/<int:id>/', mentor_info, name='mentor-info'),
    path('mentor-enroll1/', mentor_enroll, name='mentor-enroll'),
    path('mentor-enroll2/', mentor_enroll2, name='mentor-enroll2'),
    path('mentor-enroll3/', mentor_enroll3, name='mentor-enroll3'),
    path('mentor-ask', mentor_ask, name='mentor-ask'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)