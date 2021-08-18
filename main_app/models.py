from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
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

RARITIES = (
    ('1', 'Common'),
    ('2', 'Uncommon'),
    ('3', 'Rare'),
    ('4', 'Holo Rare'),
    ('5', 'Reverse Holo'),
    ('6', 'Secret Rare'),
    ('7', 'Rainbow Rare'),
    ('8', 'Promotional'),
    ('9', 'Does Not Apply'),
)

STATUS = (
    ('1', 'EX'),
    ('2', 'GX'),
    ('3', 'Tag Team'),
    ('4', 'VMAX'),
    ('5', 'Full Art'),
    ('6', 'Full Body'),
    ('7', 'Half Art'),
    ('8', 'Half Body '),
    ('9', 'V'),
    ('10', 'Does Not Apply'),
)
# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('types_detail', kwargs={'pk': self.id})
    
class Card(models.Model):
    name = models.CharField(max_length=100)
    types = models.ManyToManyField(Type)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'card_id': self.id})
    
class CardSet(models.Model):
    card_set_name = models.CharField(max_length=200, default="None")
    name = models.CharField(max_length=200)
    rarity = models.CharField(max_length=100, choices=RARITIES, default="Common")
    status = models.CharField(max_length=100, choices=STATUS, default="Ex: Full-Art, Half-Art, etc...")
    condition = models.CharField(max_length=2, choices=CONDITIONS, default=[0][0])
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_condition_display()} in {self.name}"

