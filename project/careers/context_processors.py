# careers/context_processors.py

from django.contrib.auth.models import User

def bookmark_counts(request):
    if request.user.is_authenticated:
        ci_bm_count = request.user.ci_bms.count()
        cp_bm_count = request.user.cp_bms.count()
        ei_bm_count = request.user.ei_bms.count()
        total_bm_count = ci_bm_count + cp_bm_count + ei_bm_count
    else:
        total_bm_count = 0
    
    return {
        'total_bm_count': total_bm_count,
    }
