from django.db import models

# Create your models here.
class url(models.Model):
    # link will take the url that we'll give to shorten
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=50)    
