from django.db import models

# Create your models here.

class Closet(models.Model):
    name = models.CharField(max_length=200)

class Clothes(models.Model):
    closet = models.ForeignKey(Closet, on_delete=models.CASCADE)
    id = models.CharField(max_length=30)
    type_cloth = models.CharField(max_length=200)
    size = models.CharField(max_length=200)