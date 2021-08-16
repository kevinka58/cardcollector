from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)

def __str__(self):
    return self.name

