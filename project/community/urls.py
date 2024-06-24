from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "community"
urlpatterns = [
    path('free-board/', free_board, name='free-board'),
    path('move-board/', move_board, name='move-board'),
    path('new-free/', new_free, name="new-free"),
    path('free-create/', free_create, name="free-create"),
    path('free-detail/<int:id>/', free_detail, name='free-detail'),
    path('free-edit/<int:id>/', free_edit, name="free-edit"),
    path('free-update/<int:id>/', free_update, name="free-update"),
    path('free-delete/<int:id>/', free_delete, name="free-delete"),
    path('new-move/', new_move, name="new-move"),
    path('move-create/', move_create, name="move-create"),
    path('move-detail/<int:id>/', move_detail, name='move-detail'),
    path('move-edit/<int:id>/', move_edit, name="move-edit"),
    path('move-update/<int:id>/', move_update, name="move-update"),
    path('move-delete/<int:id>/', move_delete, name="move-delete"),
    path('freetag-list', freetag_list, name="freetag-list"),
    path('movetag-list', movetag_list, name="movetag-list"),
    path('freetag-frees/<int:freetag_id>', freetag_frees, name="freetag-frees"),
    path('movetag-moves/<int:movetag_id>', movetag_moves, name="movetag-moves"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
