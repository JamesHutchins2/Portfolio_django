
from django.db import models



class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=400)
    image = models.ImageField(upload_to="images/")
    
    def summary(self):
        return self.body[:100]
    def __str__(self):
        return self.title