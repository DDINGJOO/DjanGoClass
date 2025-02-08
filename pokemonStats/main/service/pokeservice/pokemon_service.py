from common.loggingManeger.logConfig import log_message
from pokemonStats.main.data.poke_data.data_on_python.Pokemon import Pokemon, Pokemons
from pokemonStats.main.data.poke_data.data_on_databases.database_selector import database_manager

from pprint import pprint
class poke_service:
    def __init__(self):
        self.db_manager = database_manager().get_database()


    def insert_pokemons_by_number_until_number(self, number):
        pokemons = Pokemons()
        for i in range(1, number + 1):
            pokemons.add_pokemon(Pokemon(i))
        log_message("info","poke_service.insert_Pokemons_by_number_until_number",f"Inserted {number} Pokemons")
        return self.db_manager.insert_pokemons_data(pokemons.get_all_pokemons())


    def get_pokemon_by_id(self, id):
        raw_pokemon = self.db_manager.fetch_pokemon_by_number(id)
        return self._format_pokemon(raw_pokemon)

    def get_pokemon_by_name(self, name):
        raw_pokemon = self.db_manager.fetch_pokemon_by_name(name)
        return self._format_pokemon(raw_pokemon)



    def get_pokemons_by_number_ASC(self):
        raw_pokemons = self.db_manager.fetch_all_pokemons()
        return [self._format_pokemon(p) for p in raw_pokemons]

    def get_pokemons_by_name_ASC(self):
        raw_pokemons = self.db_manager.fetch_pokemons_data_query_sorted()
        return [self._format_pokemon(p) for p in raw_pokemons]

    def _format_pokemon(self, raw_pokemon):
        if raw_pokemon:
            return {
                "name": raw_pokemon[0],
                "id": raw_pokemon[1],
                "hp": raw_pokemon[2],
                "attack": raw_pokemon[3],
                "defense": raw_pokemon[4]
            }
        return None


if __name__ == '__main__':
    poke_service = poke_service()
    poke_service.insert_pokemons_by_number_until_number(11)
    pokemon = poke_service.get_pokemon_by_id(1)
    print(poke_service.get_pokemon_by_name("charizard"))



