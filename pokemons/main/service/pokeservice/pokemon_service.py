from pokemons.main.config.logConfig import log_message
from pokemons.main.data.poke_data.data_on_python.Pokemon import Pokemon, Pokemons
from pokemons.main.data.poke_data.data_on_databases.database_selector import database_manager

from pprint import pprint
class poke_service:
    def insert_pokemons_by_number_until_number(self, number):
        db_manager = database_manager().get_database()
        pokemons = Pokemons()
        for i in range(1, number + 1):
            pokemons.add_pokemon(Pokemon(i))
        db_manager.insert_pokemons_data(pokemons.get_all_pokemons())
        log_message("info","poke_service.insert_Pokemons_by_number_until_number",f"Inserted {number} Pokemons")

    def get_pokemon_by_id(self, id):
        db_manager = database_manager().get_database()
        return db_manager.fetch_pokemon_by_number(id)

    def get_pokemon_by_name(self, name):
        db_manager = database_manager().get_database()
        return db_manager.fetch_pokemon_by_name(name)


    def get_pokemons_by_number_ASC(self):
        db_manager = database_manager().get_database()
        return db_manager.fetch_all_pokemons()

    def get_pokemons_by_name_ASC(self):
        db_manager = database_manager().get_database()
        return db_manager.fetch_pokemons_data_query_sorted()


if __name__ == '__main__':
    poke_service = poke_service()
    # poke_service.insert_pokemons_by_number_until_number(11)
    print(poke_service.get_pokemon_by_id(10))
    pprint(poke_service.get_pokemons_by_number_ASC())
    print(poke_service.get_pokemon_by_name("charizard"))
    pprint(poke_service.get_pokemons_by_name_ASC())


