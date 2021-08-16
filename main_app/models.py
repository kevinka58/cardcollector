from django.db import models
from django.urls import reverse

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'card_id': self.id})

