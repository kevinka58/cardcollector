from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class Card:
    def __init__(self, name, rarity, status, condition):
        self.name = name
        self.rarity = rarity
        self.status = status
        self.condition = condition

cards = [
    Card('Charizard: V-Max', 'Ultra Rare', 'Full Art', 'PSA-9'),
    Card('Reshiram', 'Amazing Rare', 'Holographic', 'PSA-10'),
    Card("Brock's Grit", "Rare", "Holographic", "PSA-9"),
]



def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def about(request):
    return render(request, "about.html")

def cards_index(request):
    return render(request, 'cards/index.html', {'cards': cards})
