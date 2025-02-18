"""
URL configuration for PokeDexSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from PokeDexSite.views import pokedex_view, PokedexInitView

urlpatterns = [
    path('api/pokedex', include('pokeDex.controller.urls')),
    path('api/pokedeximage', include('pokeDexImages.controller.urls')),

    path('api', include('comment.urls')),
    path('api/setup/pokedex/<int:number>',PokedexInitView.as_view()),



    path('pokedex/<int:number>', pokedex_view, name='pokedex_view'),

]
