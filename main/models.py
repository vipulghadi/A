from django.db import models

# Create your models here.
class BlogPost(models.Model):
    Title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    publish_on =models.DateField(auto_now=True)
    Description=models.TextField()
