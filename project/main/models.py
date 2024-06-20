from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile

# Create your models here.

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mentor_company = models.CharField(max_length=50)
    mentor_dept = models.CharField(max_length=50)
    mentor_work = models.CharField(max_length=50)
    
    mentor_summary = models.CharField(max_length=50)
    mentor_info = models.TextField(max_length=300)
    mentor_career = models.CharField(max_length=50)

    mentor_certificate = models.CharField(max_length=100, null=True, blank=True)
    mentor_id_card = models.ImageField(upload_to="mentor_1/")
    mentor_name_card = models.ImageField(upload_to="mentor_2/")
    
    mentor_at = models.DateTimeField()

    def __str__(self):
        return self.mentor_intro[:30]