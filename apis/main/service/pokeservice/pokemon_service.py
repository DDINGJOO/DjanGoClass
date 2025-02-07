from apis.main.pokemons_data.data_on_python.Pokemon import Pokemon, Pokemons
from apis.main.pokemons_data.data_on_databases.database_selector import database_manager

class poke_service:
    def insert_Pokemons_by_number_until_number(self, number):
        for i in range(1, number + 1):
            pokemons = Pokemons()
            pokemons.add_pokemon(Pokemon(i))
            db_manager = database_manager().get_database()
            db_manager.insert_pokemons_data(pokemons.get_all_pokemons())


if __name__ == '__main__':
    poke_service = poke_service()
    poke_service.insert_Pokemons_by_number_until_number(11)

