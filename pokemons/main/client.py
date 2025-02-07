from pokemons.main.service.pokeservice.pokemon_service import  poke_service
if __name__ == "__main__":
    poke_service = poke_service()
    poke_service.insert_Pokemons_by_number_until_number(20)

##   Client PostCall API for insertPokemons until set number ascendant
##   url    = "http://DNS.com/api/insertPokemons/{number} -> 15
##
##   Server Call API for insertPokemons until set number asc
##      Method insert_Pokemons_by_number_until_number