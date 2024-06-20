from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50, default='')
    user_phone = models.CharField(max_length=50, default='')
    user_birth = models.DateField(default='2000-01-01')
    user_major = models.CharField(max_length=100, blank=True, null=True, default='')
    user_profile = models.ImageField(upload_to="profile/", null=True, blank=True)
    ENROLL_CHOICES = [
        ('재학', '재학'),
        ('휴학', '휴학'),
        ('졸업', '졸업'),
        ('교직원', '교직원'),
    ]
    user_enroll = models.CharField(max_length=50, blank=True, null=True, choices=ENROLL_CHOICES, default='')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
