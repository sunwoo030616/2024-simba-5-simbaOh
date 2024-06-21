from django.contrib import admin
from .models import Free, Move, Freecomment, Movecomment, Freetag, Movetag
# Register your models here.
admin.site.register(Free)
admin.site.register(Move)
admin.site.register(Freecomment)
admin.site.register(Movecomment)
admin.site.register(Freetag)
admin.site.register(Movetag)