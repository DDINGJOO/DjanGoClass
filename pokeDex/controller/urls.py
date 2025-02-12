
from django.urls import path
from .views import PokeDexInsertView, PokeDexByIdView, PokeDexBySortByNameView, PokeDexListView, PokeDexByNameView

urlpatterns = [
    path('/post/number/<int:number>', PokeDexInsertView.as_view()),
    path('/get/name/<str:name>/', PokeDexByNameView.as_view()),
    path('/get/number/<int:number>/', PokeDexByIdView.as_view()),
    path('/list/name/<str:name>/', PokeDexBySortByNameView.as_view()),
    path('/list/number/<str:order>/', PokeDexListView.as_view()),
]

