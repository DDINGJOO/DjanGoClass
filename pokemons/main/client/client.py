from pokemons.main.service.pokeservice.pokemon_service import  poke_service
if __name__ == "__main__":
    poke_service = poke_service()
    poke_service.insert_pokemons_by_number_until_number(20)
    poke_service.get_pokemon_by_id(3)
    poke_service.get_pokemons_by_name_ASC()

##   Client PostCall API for insertPokemons until set number ascendant
##   url    = "http://DNS.com/api/insertPokemons/{number} -> 15
##
##   Server Call API for insertPokemons until set number asc
##      Method insert_Pokemons_by_number_until_number