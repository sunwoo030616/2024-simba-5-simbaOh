from django.db import models
from django.contrib.auth.models import User

class Careerinfotag(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name
    
class Careerprogramtag(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name


# Create your models here.
class Careerinfo(models.Model):

    title = models.CharField(max_length=50)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    company = models.CharField(max_length=30)
    field = models.CharField(max_length=10)
    content = models.TextField()
    startline = models.CharField(max_length=20, default='')
    deadline = models.CharField(max_length=20)
    image=models.ImageField(upload_to="careerinfo/", blank=True, null=True)
    pub_date = models.DateTimeField()
    careerinfotags=models.ManyToManyField(Careerinfotag, related_name='careerinfos', blank=True)
    ci_bm= models.ManyToManyField(User, related_name='ci_bms', blank=True)
    cibm_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

class Careerprogram(models.Model):

    title = models.CharField(max_length=50)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    startline = models.CharField(max_length=20, default='')
    deadline = models.CharField(max_length=20)
    place = models.CharField(max_length=30)
    field = models.CharField(max_length=10)
    content = models.TextField()
    image=models.ImageField(upload_to="careerprogram/", blank=True, null=True)
    pub_date = models.DateTimeField()
    careerprogramtags=models.ManyToManyField(Careerprogramtag, related_name='careerprograms', blank=True)
    cp_bm= models.ManyToManyField(User, related_name='cp_bms', blank=True)
    cpbm_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

