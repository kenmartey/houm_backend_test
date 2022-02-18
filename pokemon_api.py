import os
import requests

# dotenv import and settings
from dotenv import load_dotenv
load_dotenv()


class PokemonAPI:
    """Base class for Pokemon api"""

    def __init__(self):
        self.base_url = os.getenv("POKEMON_BASE_URL")
        self.header = {'content-type': 'application/json'}

    def get_pokemons(self):
        """Get list of pokemon names. Pass in limit value for pagination"""
        pokemon_names = []
        response = requests.get(
            f"{self.base_url}/pokemon?limit=200", headers=self.header)
        response = response.json()
        for i in response["results"]:
            pokemon_names.append(i.get("name"))
        return pokemon_names

    def check_string_letter_repititon(self):
        """String operation to grab only names with at and 2 (a)'s"""
        names = self.get_pokemons()
        count = 0
        for i in names:
            if "a" in i and "at" in i:
                if i.count("a") > 1:
                    count += 1
        return count

    def pokemon_breed(self):
        """Return breeds and eliminate self named breed"""
        breeds = []
        response = requests.get(
            f"{self.base_url}/egg-group/6/", headers=self.header)
        response = response.json()
        for i in response["pokemon_species"]:
            breeds.append(i.get("name"))
        breeds.remove('raichu')
        return len(breeds)

pokemon = PokemonAPI()
print(pokemon.check_string_letter_repititon())
print(pokemon.pokemon_breed())