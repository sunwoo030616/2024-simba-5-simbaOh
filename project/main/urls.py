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
    path('mentor-create/', mentor_create, name='mentor-create'),
    path('mentor-enroll/', mentor_enroll, name='mentor-enroll'),
    path('mentor-ask/<int:id>/', mentor_ask, name='mentor-ask'),
    path('follows/<int:mentor_id>/', follows, name='follows'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
