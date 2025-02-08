from rest_framework.response import Response
from rest_framework.views import APIView
from pokemonStats.main.service.pokeservice.pokemon_service import poke_service  # 기존 서비스 가져오기

from rest_framework.response import Response
from rest_framework.views import APIView
from pokemonStats.main.service.pokeservice.pokemon_service import poke_service  # 기존 서비스 가져오기

class PokemonInsertView(APIView):


    def post(self, request,number):
        number = request.data.get("number", number)  # 기본값 10개 추가
        service = poke_service()
        service.insert_pokemons_by_number_until_number(number)
        return Response({"message": f"Inserted {number} Pokemons"}, status=201)

class PokemonByIdView(APIView):


    def get(self, request, number):
        service = poke_service()
        pokemon = service.get_pokemon_by_id(int(number))
        return Response(pokemon)

class PokemonByNameView(APIView):


    def get(self, request, name):
        service = poke_service()
        pokemon = service.get_pokemon_by_name(name)
        return Response(pokemon)

class PokemonListView(APIView):

    def get(self, request, order="number"):
        service = poke_service()
        if order == "name":
            pokemons = service.get_pokemons_by_name_ASC()
        else:
            pokemons = service.get_pokemons_by_number_ASC()
        return Response(pokemons)

