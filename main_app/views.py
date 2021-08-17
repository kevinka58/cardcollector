from main_app.forms import CardSetForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Card
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def about(request):
    return render(request, "about.html")

def cards_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {'cards': cards})

def cards_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    card_set_form = CardSetForm
    return render(request, 'cards/detail.html', {'card': card, 'card_set_form': card_set_form})

def add_cardset(request, card_id):
    form = CardSetForm(request.POST)
    if form.is_valid():
        new_card_set = form.save(commit=False)
        new_card_set.card_id = card_id
        new_card_set.save()
    return redirect('detail', card_id=card_id)

class CardCreate(CreateView):
    model = Card
    fields = '__all__'

class CardUpdate(UpdateView):
    model = Card
    fields = ['rarity', 'status', 'condition']

class CardDelete(DeleteView):
    model = Card
    success_url = '/cards/'