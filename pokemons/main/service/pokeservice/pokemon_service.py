from pokemons.main.config.logConfig import log_message
from pokemons.main.pokemons_data.data_on_python.Pokemon import Pokemon, Pokemons
from pokemons.main.pokemons_data.data_on_databases.database_selector import database_manager

class poke_service:
    def insert_Pokemons_by_number_until_number(self, number):
        db_manager = database_manager().get_database()
        pokemons = Pokemons()
        for i in range(1, number + 1):
            pokemons.add_pokemon(Pokemon(i))
        db_manager.insert_pokemons_data(pokemons.get_all_pokemons())
        log_message("info","poke_service.insert_Pokemons_by_number_until_number",f"Inserted {number} Pokemons")


if __name__ == '__main__':
    poke_service = poke_service()
    poke_service.insert_Pokemons_by_number_until_number(11)

