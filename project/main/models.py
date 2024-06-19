from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mentor(models.Model):
    # mentor_name = models.OneToOneField(User, on_delete=models.CASCADE)

    mentor_company = models.CharField(max_length=50)
    mentor_dept = models.CharField(max_length=50)
    mentor_work = models.CharField(max_length=50)
    
    mentor_intro = models.CharField(max_length=300)
    mentor_year = models.IntegerField()

    mentor_at = models.DateTimeField()

    def __str__(self):
        return f"{self.mentor_company} - {self.mentor_dept} : {self.mentor_intro[:30]}..."