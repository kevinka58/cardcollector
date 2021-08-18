from main_app.forms import CardSetForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Card, CardSet, Type
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def about(request):
    return render(request, "about.html")

@login_required
def cards_index(request):
    cards = Card.objects.filter(user = request.user)
    return render(request, 'cards/index.html', {'cards': cards})

@login_required
def cards_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    types_card_doesnt_have = Type.objects.exclude(id__in = card.types.all().values_list('id'))
    card_set_form = CardSetForm
    return render(request, 'cards/detail.html', {
        'card': card,
        'card_set_form': card_set_form,
        'types': types_card_doesnt_have,
         })

@login_required
def add_cardset(request, card_id):
    form = CardSetForm(request.POST)
    if form.is_valid():
        new_card_set = form.save(commit=False)
        new_card_set.card_id = card_id
        new_card_set.save()
    return redirect('detail', card_id=card_id)
    
@login_required
def delete_cardset(request, card_id, cardset_id):
    card = Card.objects.get(id=card_id)
    cardset = CardSet.objects.get(card_id=card_id, id=cardset_id)
    card.cardset_set.remove(cardset)
    return redirect('detail', card_id=card_id)

class CardCreate(CreateView):
    model = Card
    fields = '__all__'

    # This inherited method is called when a valid vat form is being submitted
    def form_valid(self, form):
        # Assig the logged in user (self.request.user)
        form.instance.user = self.request.user # form.instance is the cat
        return super().form_valid(form)

class CardUpdate(LoginRequiredMixin, UpdateView):
    model = Card
    fields = ['rarity', 'status', 'condition']

class CardDelete(LoginRequiredMixin, DeleteView):
    model = Card
    success_url = '/cards/'

class TypeList(LoginRequiredMixin, ListView):
    model = Type

class TypeDetail(LoginRequiredMixin, DetailView):
    model = Type

class TypeCreate(LoginRequiredMixin, CreateView):
    model = Type
    fields = '__all__'

class TypeUpdate(LoginRequiredMixin, UpdateView):
    model = Type
    fields = ['name', 'color']

class TypeDelete(LoginRequiredMixin, DeleteView):
    model = Type
    success_url = '/types/'

@login_required
def assoc_type(request, card_id, type_id):
    Card.objects.get(id=card_id).types.add(type_id)
    return redirect('details', card_id=card_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object that includes the date from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #This will add the user to database
            user = form.save()
            #This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
        # A bad POST or a GET request, so render signup.html with an empty form
        form = UserCreationForm()
        context = {'form': form, 'error_message': error_message}
        return render (request, 'registration/signup.html', context)