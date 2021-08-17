from django.db import models
from django.urls import reverse

CONDITIONS = (
    ('1', 'PSA-1'),
    ('2', 'PSA-2'),
    ('3', 'PSA-3'),
    ('4', 'PSA-4'),
    ('5', 'PSA-5'),
    ('6', 'PSA-6'),
    ('7', 'PSA-7'),
    ('8', 'PSA-8'),
    ('9', 'PSA-9'),
    ('10', 'PSA-10'),
)
# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=100)
  

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'card_id': self.id})
    
class CardSet(models.Model):
    card_set_name = models.CharField(max_length=200, default="None")
    name = models.CharField(max_length=200)
    rarity = models.CharField(max_length=100, default="Common")
    status = models.CharField(max_length=100, default="Ex: Full-Art, Half-Art, etc...")
    condition = models.CharField(max_length=2, choices=CONDITIONS, default=[0][0])
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_condition_display()} in {self.name}"

