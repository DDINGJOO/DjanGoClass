from pokemons.main.pokemons_data.data_on_databases.pokemon_database_interface import pokemon_datebase
import sqlite3
import os




class pokemon_sqlite3(pokemon_datebase):

    def __init__(self):
        super().__init__()


        self.DB_PATH = os.getenv("POKEMON_DB_PATH", "default.db")
        self.COMMANDS = \
            {"create_pokemon_table_query":
                 """
                 CREATE TABLE IF NOT EXISTS pokemon (
                 Name TEXT NOT NULL,
                 Number INTEGER PRIMARY KEY,
                 Hp INTEGER NOT NULL,
                 Attack INTEGER NOT NULL,
                 Defense INTEGER NOT NULL)""",
             "insert_pokemons_data_query":
                 """
                 INSERT OR IGNORE INTO pokemon (Name, Number, Hp, Attack, Defense)
                 VALUES (?, ?, ?, ?, ?)""",
             "fetch_pokemons_data_query":
                 """
                 SELECT * FROM pokemon""",
             "fetch_pokemon_by_number_query":"""
                 SELECT * FROM pokemon WHERE Number = ?
                 """}





    def setup_pokemon_database(self):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(self.COMMANDS.get("create_pokemon_table_query"))
            conn.commit()



    def insert_pokemons_data(self,poke_list):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.executemany(
                self.COMMANDS.get("insert_pokemons_data_query"),
                [(p["Name"], p["Number"], p["Hp"], p["Attack"], p["Defense"]) for p in poke_list],
            )
            conn.commit()


    def fetch_all_pokemons(self):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(self.COMMANDS.get("fetch_pokemons_data_query"))
            data = cursor.fetchall()
            return data


    def fetch_pokemon_by_number(self, number):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(self.COMMANDS.get("fetch_pokemon_by_number_query"), (number,))
            data = cursor.fetchone()
            return data



if __name__ == "__main__":

    database = pokemon_sqlite3()
    database.setup_pokemon_database()
    # 데이터 입력
    pokemon_data = [
        {"Name": "Pikachu", "Number": 25, "Hp": 35, "Attack": 55, "Defense": 40},
        {"Name": "Squirtle", "Number": 7, "Hp": 48, "Attack": 65, "Defense": 65},
        {"Name": "Charmander", "Number": 4, "Hp": 39, "Attack": 52, "Defense": 43},
    ]
    database.insert_pokemons_data(pokemon_data)


    print(database.fetch_pokemon_by_number(25))
    print(database.fetch_all_pokemons())





