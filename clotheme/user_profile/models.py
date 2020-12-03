from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200, default='')
    password = models.CharField(max_length=200, default='')
    profile_pic = models.CharField(max_length=1000, default='')

