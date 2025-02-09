from rest_framework.response import Response
from rest_framework.views import APIView
from pokeDex.service.PokeDexService import PokeDexService  # 기존 서비스 가져오기


## TODO : Using Cache!
class PokeDexInsertView(APIView):
    def post(self, request,number):
        number = request.data.get("number", number)  # 기본값 10개 추가
        service = PokeDexService()
        service.insert_pokemons_by_number_until_number(number)
        return Response({"message": f"Inserted {number} Pokemons"}, status=201)

class PokeDexByIdView(APIView):
    def get(self, request, number):
        service = PokeDexService()
        pokemon = service.get_pokemon_by_id(int(number))
        return Response(pokemon)

class PokeDexBySortByNameView(APIView):

    def get(self, request, name):
        service = PokeDexService()
        pokemon = service.get_pokemon_by_name(name)
        return Response(pokemon)

class PokeDexListView(APIView):

    def get(self, request, order="number"):
        service = PokeDexService()
        if order == "name":
            pokemons = service.get_pokemons_by_name_ASC()
        if order == "number":
            pokemons = service.get_pokemons_by_number_ASC()
        else:
            return Response(None)
        return Response(pokemons)

class PokeDexByNameView(APIView):
    def get(self, request, name):
        service = PokeDexService()
        pokemon = service.get_pokemon_by_name(str(name))
        return Response(pokemon)



