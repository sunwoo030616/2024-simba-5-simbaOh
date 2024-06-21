from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path('mypage/<int:id>/', mypage, name="mypage"),
    path('edit_portfolio/', edit_portfolio, name='edit_portfolio'),
    path('follow-list/<int:id>', follow_list, name="follow-list")
]