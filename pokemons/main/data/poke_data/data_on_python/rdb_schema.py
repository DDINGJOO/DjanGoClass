import sqlite3

# 데이터베이스 테이블 생성 쿼리 (오류 수정)
create_pokemon_table_query = """
    CREATE TABLE IF NOT EXISTS pokemon (
        Name TEXT NOT NULL,
        Number INTEGER PRIMARY KEY,
        Hp INTEGER NOT NULL,
        Attack INTEGER NOT NULL,
        Defense INTEGER NOT NULL
    )
"""

# 데이터 삽입 쿼리 (OR IGNORE → OR REPLACE 사용 가능)
insert_pokemon_data_query = """
    INSERT OR IGNORE INTO pokemon (Name, Number, Hp, Attack, Defense)
    VALUES (?, ?, ?, ?, ?)
"""

# 데이터 조회 쿼리
fetch_pokemon_data_query = """
    SELECT * FROM pokemon
"""



# 데이터베이스 파일명
DB_NAME = "pokemon.db"
def setup_pokemon_database():
    """ 데이터베이스 및 테이블 생성 """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(create_pokemon_table_query)
        conn.commit()


def insert_pokemon_data(poke_list):
    """ 포켓몬 데이터를 데이터베이스에 삽입 """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.executemany(
            insert_pokemon_data_query,
            [(p["Name"], p["Number"], p["Hp"], p["Attack"], p["Defense"]) for p in poke_list],
        )
        conn.commit()


def fetch_all_pokemon():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(fetch_pokemon_data_query)
        data = cursor.fetchall()
        return data



## TESTING

# 샘플 데이터
pokemon_data = [
    {"Name": "Pikachu", "Number": 25, "Hp": 35, "Attack": 55, "Defense": 40},
    {"Name": "Squirtle", "Number": 7, "Hp": 44, "Attack": 48, "Defense": 65},
    {"Name": "Charmander", "Number": 4, "Hp": 39, "Attack": 52, "Defense": 43},
    {"Name": "Pikachu", "Number": 25, "Hp": 36, "Attack": 55, "Defense": 40},  # 중복 데이터
]

## TESTING
if __name__ == "__main__":
    setup_pokemon_database()
    insert_pokemon_data(pokemon_data)

    # 데이터 조회
    print("=== 저장된 포켓몬 데이터 ===")
    for pokemon in fetch_all_pokemon():
        print(pokemon)

