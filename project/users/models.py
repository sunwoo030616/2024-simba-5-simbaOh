from django.db import models
from django.contrib.auth.models import User

class Education(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Experience(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Certification(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    introduction = models.TextField(max_length=500)
    education = models.ManyToManyField(Education)
    experience = models.ManyToManyField(Experience)
    projects = models.ManyToManyField(Project)
    certifications = models.ManyToManyField(Certification)

    def __str__(self):
        return self.user.username
