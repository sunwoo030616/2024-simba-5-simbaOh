from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mentor_company = models.CharField(max_length=50, default='')
    mentor_dept = models.CharField(max_length=50, default='')
    mentor_work = models.CharField(max_length=50, default='')
    mentor_summary = models.CharField(max_length=50, default='')  # 추가된 필드
    mentor_info = models.TextField(max_length=300, default='')
    mentor_career = models.CharField(max_length=50, default='')
    mentor_certificate = models.CharField(max_length=100, null=True, blank=True, default='')
    mentor_id_card = models.ImageField(upload_to="mentor_1/", default='')
    mentor_name_card = models.ImageField(upload_to="mentor_2/", default='')
    mentor_at = models.DateTimeField()

    def __str__(self):
        return self.mentor_summary[:30]  # mentor_intro를 mentor_summary로 수정
