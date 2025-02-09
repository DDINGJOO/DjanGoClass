from django.shortcuts import render
import requests

def pokemon_list(request):
    api_url = "http://localhost:8000/api/pokemons/list/number/"
    response = requests.get(api_url)  # API 호출 -> {id: stats}
    pokemons = response.json() if response.status_code == 200 else []


    return render(request, 'pokeDex.html', {"pokemons": pokemons})