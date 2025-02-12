from pokeDexImages.config.database_selector import DataBaseSelector
from pokeDexImages.entity.PokeDexImage import PokeDexImage
from pokeDexImages.repository.impl.PokeDexImageSqlite3 import PokeDexImageSqlite3


## TODO : Transaction impl?

class PokeDexImageService:
    def __init__(self):
        self.db_manager = DataBaseSelector().get_database()


    def set_pokemon_image_by_id(self, poke_id):
        pokemon = PokeDexImage(poke_id)
        self.db_manager.save(pokemon.pokemon_id)



##TODO : DATA SERIALIZATION & DESERIALIZATION
    def get_pokemon_image_by_id(self, poke_id):
        return self._format_data(self.db_manager.find_by_id(poke_id))


    def delete_pokemon_image_by_id(self, poke_id):

        pokemon = PokeDexImage(poke_id)
        pokemon.delete_image()
        self.db_manager.delete_by_id(poke_id)

    def get_pokemons_images(self):
        return [self._format_data(data) for data in self.db_manager.get_all_pokemons_images()]


    def _format_data(self, data):
        return {
            "id": data[0],
            "image": data[1]
        }


if __name__ == "__main__":
    service = PokeDexImageService()
    for i in range(1, 20):
        service.set_pokemon_image_by_id(i)

