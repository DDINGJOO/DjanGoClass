
from django.urls import path
from .views import PokemonInsertView, PokemonByIdView, PokemonByNameView, PokemonListView

urlpatterns = [
    path('pokemons/insert/until/<int:number>', PokemonInsertView.as_view()),
    path('pokemons/<int:number>/', PokemonByIdView.as_view()),
    path('pokemons/name/<str:name>/', PokemonByNameView.as_view()),
    path('pokemons/list/<str:order>/', PokemonListView.as_view()),
]

