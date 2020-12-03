from django.db import models

class Closet(models.Model):
    name = models.CharField(max_length=200, default='First Closet')

    

class Clothes(models.Model):
    closet = models.ForeignKey(Closet, on_delete=models.CASCADE),
    clothes_id = models.CharField(max_length=30),
    type_cloth = models.CharField(max_length=200),
    size = models.CharField(max_length=200),

    
