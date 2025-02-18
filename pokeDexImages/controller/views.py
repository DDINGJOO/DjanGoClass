from rest_framework.views import APIView

from pokeDexImages.service.PokeDexImageService import PokeDexImageService
from rest_framework.response import Response

class PokeDexImageView(APIView):
    def get(self, request, number):
        service = PokeDexImageService()
        pokemon_image = service.get_pokemon_image_by_id(int(number))
        return Response(pokemon_image)

class PokeDexImagePostView(APIView):
    def get(self, request, number):
        service = PokeDexImageService()
        pokemon_image = service.set_pokemon_image_by_id(int(number))
        return Response(status=201)


class PokeDexImageDeleteView(APIView):
    def get(self, request, number):
        PokeDexImageService().delete_pokemon_image_by_id(int(number))
        return Response(status=204)

class PokeDexImagesView(APIView):
    def get(self, request):
        service = PokeDexImageService()
        pokemon_images = service.get_pokemons_images()
        return Response(pokemon_images)
