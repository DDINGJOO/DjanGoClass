
from django.urls import path
from .views import PokeDexInsertView, PokeDexByIdView, PokeDexBySortByNameView, PokeDexListView, PokeDexByNameView

urlpatterns = [
    path('pokedex/insert/until/<int:number>', PokeDexInsertView.as_view()),
    path('pokedex/name/<str:name>/', PokeDexByNameView.as_view()),
    path('pokedex/number/<int:number>/', PokeDexByIdView.as_view()),
    path('pokedex/name/<str:name>/', PokeDexBySortByNameView.as_view()),
    path('pokedex/list/<str:order>/', PokeDexListView.as_view()),
]

