from django.forms import ModelForm, fields
from .models import CardSet

class CardSetForm(ModelForm):
    class Meta:
        model = CardSet
        fields = ['card_set_name','name', 'rarity', 'status', 'condition']