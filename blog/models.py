from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() 
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    Category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=100)