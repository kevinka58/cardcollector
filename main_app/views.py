from main_app.forms import CardSetForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Card, Type
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def about(request):
    return render(request, "about.html")

def cards_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {'cards': cards})

def cards_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    types_card_doesnt_have = Type.objects.exclude(id__in = card.types.all().values_list('id'))
    card_set_form = CardSetForm
    return render(request, 'cards/detail.html', {
        'card': card,
        'card_set_form': card_set_form,
        'types': types_card_doesnt_have,
         })

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

class TypeList(ListView):
    model = Type

class TypeDetail(DetailView):
    model = Type

class TypeCreate(CreateView):
    model = Type
    fields = '__all__'

class TypeUpdate(UpdateView):
    model = Type
    fields = ['name', 'color']

class TypeDelete(DeleteView):
    model = Type
    success_url = '/types/'

def assoc_type(request, card_id, type_id):
    Card.objects.get(id=card_id).types.add(type_id)
    return redirect('details', card_id=card_id)