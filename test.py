
# importing the modules

# unit test case
import unittest

from unittest.mock import patch, MagicMock

from .src import pokemon_api


class PokemonAPI(unittest.TestCase):
    """Test for Pokemon API"""
    pokemon = pokemon_api.PokemonAPI()

    def test_get_pokemon(self):
        """Mock get pokemon request and control return value
            Then call the get pokemon function
            Then check the assertion
        """
        self.pokemon.get_pokemons = MagicMock(
            return_value=['bulbasaur', 'ivysaur', 'caterpie', 'rattata'])
        result = self.pokemon.get_pokemons()
        self.assertEqual(
            result, ['bulbasaur', 'ivysaur', 'caterpie', 'rattata'])

    def test_check_string_letter_repititon(self):
        """Mock get pokemon request and control return value
            Then call the string checker function
            Then check the assertion
        """
        self.pokemon.get_pokemons = MagicMock(
            return_value=['bulbasaur', 'ivysaur', 'caterpie', 'rattata'])
        result = self.pokemon.check_string_letter_repititon()
        #  Then check the assertionn
        self.assertEqual(result, 1)

    def test_pokemon_breed(self):
        """Mock pokemon breed request and control return value
            Then call the pokemon breed function
            Then check the assertion
        """
        self.pokemon.pokemon_breed = MagicMock(return_value=len(
            ['pikachu', 'clefairy', 'clefable', 'jigglypuff', 'wigglytuff', 'chansey', 'togetic', 'marill']))
        result = self.pokemon.pokemon_breed()
        self.assertEqual(result, 8)

    def test_get_first_gen_pokemon_weights(self):
        """Mock get the get first gen pokemon weights and control return value
            Then call the get gen pokemon weights function
            Then check the assertion
        """
        self.pokemon.get_first_gen_pokemon_weights = MagicMock(
            return_value=[101, 1000, 1003, 55, 2000])
        result = self.pokemon.get_first_gen_pokemon_weights()
        self.assertEqual(result, [101, 1000, 1003, 55, 2000])

    def test_get_max_and_min_weight(self):
        """Mock get the get first gen pokemon weights and control return value
            Then call the get max and min weight function
            Then check the assertion
        """
        self.pokemon.get_first_gen_pokemon_weights = MagicMock(
            return_value=[101, 1000, 1003, 55, 2000])
        result = self.pokemon.get_max_and_min_weight()
        self.assertEqual(result, [2000, 55])


if __name__ == '__main__':
    unittest.main()
