from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=400)
    image = models.ImageField(upload_to="images/")