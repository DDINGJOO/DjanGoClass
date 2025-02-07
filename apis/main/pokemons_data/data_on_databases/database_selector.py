from dotenv import load_dotenv
import os
from apis.main.config.logConfig import log_message

class database_manager:
    def __init__(self):
        self.db_name = os.environ.get('DB_NAME')

    def get_database(self):
        if self.db_name == "SQLite3":
            log_message("info", "database_manager", "using SQLite3 database")
            from apis.main.pokemons_data.data_on_databases.pokemon_sqlite3 import pokemon_sqlite3
            pokemon_sqlite3().setup_pokemon_database()
            return pokemon_sqlite3()

        if self.db_name == "MYSQL":
            print("아직 지원 준비중 ..ㅠ")
            return None

        else:
            log_message("error", "Database_manager.setup_database", "db_name is empty check environment variable")
            return None

## TEST

if __name__ == "__main__":
    database_manager().get_database()