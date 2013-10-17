
from django.db import models

# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    techstack = models.TextField()
    git_link = models.TextField()
    website_link = models.TextField()
    
    
  
