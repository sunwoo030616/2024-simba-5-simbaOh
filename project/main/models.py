from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    def __str__(self):
        return self.name

class Mentor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mentor_company = models.CharField(max_length=50)
    mentor_dept = models.CharField(max_length=50)
    mentor_work = models.CharField(max_length=50)
    
    mentor_summary = models.CharField(max_length=50)
    mentor_info = models.TextField(max_length=300)
    mentor_career = models.CharField(max_length=50)

    mentor_certificate = models.CharField(max_length=100, null=True, blank=True)
    mentor_id_card = models.ImageField(upload_to="mentor_1/")
    mentor_name_card = models.ImageField(upload_to="mentor_2/")

    # follow = models.ManyToManyField(User, related_name='follow', blank=True)
    # follow_count = models.PositiveIntegerField(default=0)
    
    mentor_at = models.DateTimeField()
    followers = models.ManyToManyField(User, related_name='mentor_followings', blank=True)

    categories = models.ManyToManyField(Category, related_name='mentors', blank=True)
    mentor_ship = models.ManyToManyField(User, related_name='menti_ship', symmetrical=False, blank=True)
    def __str__(self):
        return self.mentor_info[:30]

# class Accept(models.Model):
#     mentor_ship = models.ForeignKey(Mentor, related_name='menti_ship', on_delete=models.CASCADE, blank=True, null=True, default='0')

# @receiver(post_save, sender=Mentor)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=Mentor)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()