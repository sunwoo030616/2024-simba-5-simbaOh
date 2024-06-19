from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    introduction = models.TextField(max_length=500)
    education = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    projects = models.CharField(max_length=200)
    certifications = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

