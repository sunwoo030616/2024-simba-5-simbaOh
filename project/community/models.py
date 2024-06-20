from django.db import models

# Create your models here.
class Community(models.Model):
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=30)
    body=models.TextField()
    pub_date=models.DateTimeField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]