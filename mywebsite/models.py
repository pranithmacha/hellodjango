
from django.db import models

# Create your models here.

class MyProjects(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    techstack = models.TextField()
    git_link = models.TextField()
    website_link = models.TextField()
    
    class Meta:
        verbose_name_plural = "My Projects"
  
