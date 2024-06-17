from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=50)
    user_birth = models.DateField()
    user_major = models.CharField(max_length=100, blank=True)
    user_profile=models.ImageField(upload_to='images/', null=True, blank=True)
    user_enroll= models.CharField(max_length=50, blank=True)
    updated_at=models.DateTimeField()

