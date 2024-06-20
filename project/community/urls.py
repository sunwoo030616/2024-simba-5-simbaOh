from django.contrib import admin
from django.urls import path
from .views import *

app_name = "community"
urlpatterns = [
    path('', communities, name='communities'),
    path('new-post/', new_post, name="new-post"),
    path('create/', create, name="create"),
    path('detailc/<int:id>/', detailc, name="detailc"),
    path('editc/<int:id>/', editc, name="editc"),
    path('update/<int:id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"),
]