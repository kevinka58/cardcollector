from django.contrib import admin
from .models import Card, CardSet, Type
# Register your models here.

admin.site.register(Card)
admin.site.register(CardSet)
admin.site.register(Type)