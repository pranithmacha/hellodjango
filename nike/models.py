from django.db import models

# Create your models here.

class posts(models.Model):

  data = models.CharField(max_length=20)
  name = models.CharField(max_length=20)
  userId = models.TextField()
  
