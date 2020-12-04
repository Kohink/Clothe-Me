from django.db import models
from django.urls import reverse

class Closet(models.Model):
    name = models.CharField(max_length=200, default='My Closet')
    desc = models.CharField(max_length=1000, default='Description')

    def get_absolute_url(self):
        return reverse('user_closet:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

class Clothes(models.Model):
    closet = models.ForeignKey(Closet, on_delete=models.CASCADE, default=1)
    clothes_name = models.CharField(max_length=30, default='Name')
    brand = models.CharField(max_length=30, default='Brand')
    color = models.CharField(max_length=30, default='Color')
    type_cloth = models.CharField(max_length=30, default='Cloth Type')
    size = models.CharField(max_length=30, default='Size')
    image = models.CharField(max_length=1000, default='No Image')

    def __str__(self):
        return self.clothes_name