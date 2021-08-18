from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('cards/', views.cards_index, name='index'),
    path('cards/<int:card_id>/', views.cards_detail, name='detail'),
    path('cards/create/', views.CardCreate.as_view(), name='cards_create'),
    path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name="cards_update"),
    path('cards/<int:pk>/delete/', views.CardDelete.as_view(), name="cards_delete"),
    path('cards/<int:card_id>/add_cardset/', views.add_cardset, name="add_cardset"),
    path('cards/<int:card_id>/delete_cardset/<int:cardset_id>', views.delete_cardset, name="delete_cardset"),
    path('types/', views.TypeList.as_view(), name='types_index'),
    path('types/<int:pk>/', views.TypeDetail.as_view(), name='types_detail'),
    path('types/create/', views.TypeCreate.as_view(), name='types_create'),
    path('types/<int:pk>/delete', views.TypeUpdate.as_view(), name='types_update'),
    path('types/<int:pk>/delete/', views.TypeDelete.as_view(), name='types_delete'),
    path('types/<int:card_id>/assoc_type/<int:type_id>/', views.assoc_type, name='assoc_type'),
    path('types/<int:card_id>/unassoc_type/<int:type_id>/', views.unassoc_type, name='unassoc_type'),
    path('accounts/signup/', views.signup, name="signup")
    ]
