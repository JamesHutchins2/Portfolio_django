from distutils.command.upload import upload
from email.mime import image
from django.db import models
class Job(models.Model):
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=600)
    
# Create your models here.
