from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, default="")
    profile_pics = models.ImageField(default="default.jpg", upload_to="profile_pics")