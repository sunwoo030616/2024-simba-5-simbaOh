from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "accounts"
urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('signup/', signup, name="signup"),
    path('signup2/', signup2, name="signup2"),
    path('signup3/', signup3, name="signup3"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)