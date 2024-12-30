from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() 
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=False , null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('category', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag', related_name= 'blogs')

class Tag(models.Model):
    name = models.CharField(max_length=100 , unique=True , default="") 

class Category(models.Model):
    name = models.CharField(max_length=100)