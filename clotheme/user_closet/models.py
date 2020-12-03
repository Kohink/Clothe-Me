from django.db import models
# Create your models here.

class Closet(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Clothes(models.Model):
    closet = models.ForeignKey(Closet, on_delete=models.CASCADE)
    clothing_name = models.CharField(max_length=30)
    type_cloth = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    image = models.CharField(max_length=4000)