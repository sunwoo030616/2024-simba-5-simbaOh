from django.contrib import admin
from .models import Careerinfo, Careerinfotag, Careerprogram, Careerprogramtag, Eduinfo, Eduinfotag

# Register your models here.
admin.site.register(Careerinfo)
admin.site.register(Careerinfotag)
admin.site.register(Careerprogram)
admin.site.register(Careerprogramtag)
admin.site.register(Eduinfo)
admin.site.register(Eduinfotag)