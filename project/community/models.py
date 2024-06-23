from django.db import models
from django.contrib.auth.models import User


class Freetag(models.Model):
    freename = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.freename
    
class Movetag(models.Model):
    movename = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.movename
    
class Free(models.Model):
    
    title = models.CharField(max_length=255)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    content = models.TextField()
    ftcontent=models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="free/", blank=True, null=True)
    emoji = models.TextField()
    freetags = models.ManyToManyField(Freetag, related_name='frees', blank=True)
    def __str__(self):
        return self.title

    
    def summary(self):
        return self.content[:20]

class Move(models.Model):
    
    title = models.CharField(max_length=255)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    content = models.TextField()
    mtcontent = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="move/", blank=True, null=True)
    emoji = models.TextField()
    movetags = models.ManyToManyField(Movetag, related_name='moves', blank=True)
    def __str__(self):
        return self.title

    
    def summary(self):
        return self.content[:20]
    
class Freecomment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    free = models.ForeignKey(Free, null=False, blank=False, on_delete=models.CASCADE)


    def __str__(self):
        return self.free.title + " : " + self.content[:20] + " by " + self.writer.profile.nickname
    
class Movecomment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    move = models.ForeignKey(Move, null=False, blank=False, on_delete=models.CASCADE)


    def __str__(self):
        return self.move.title + " : " + self.content[:20] + " by " + self.writer.profile.nickname
    
