from django.db import models

# Create your models here.
class Job(models.Model):
    #search in google for django model fields
    #to work with images need Pillow Package - pip install Pillow
    image=models.ImageField(upload_to='images/') #images will be saved to images folder in media
    summary=models.CharField(max_length=200)
