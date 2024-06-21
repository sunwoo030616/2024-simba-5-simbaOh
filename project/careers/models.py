from django.db import models

# Create your models here.
class Careerinfo(models.Model):

    title = models.CharField(max_length=50)
    company = models.CharField(max_length=30)
    place = models.CharField(max_length=10)
    content = models.TextField()
    deadline = models.CharField(max_length=20)
    image=models.ImageField(upload_to="careerinfo/", blank=True, null=True)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
