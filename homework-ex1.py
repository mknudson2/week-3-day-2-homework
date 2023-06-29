"""
Exercise 1:
Create a Method that prints an image of a random pokemon
HINT: You may need another attribute as well to store your image url within.
"""

from random import randint
from requests import get



class Pokemon:
    
    def __init__(self, name):
        self.name = str(randint(1, 898))
        self.weight = None
        self.types = []
        self.abilities =[]
        self.image = ' '
    
    def poke_api_call(self):
        res = get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
        if res.ok:
            data = res.json()
            self.name = data['name']
            self.abilities = data['abilities']
            self.weight = data['weight']
            self.types = data['types']
            self.image=data['sprites']['versions']['generation-v']['black-white']['animated']['front_shiny']
            if not self.image:
                self.image = data['sprites']['front_default']
    
    def poke_generator(self):
        random_pokemon = [randint(1,898) for i in range(6)]
    
    def display_pokemon_info(self):
        self.display_pokemon_image()
        print(f'{self.name}')
        
    
    def display_pokemon_image(self, width=150):
        display(Image(self.image, width = width))
    
starter = Pokemon(random_pokemon)

random_pokemon.display_pokemon_info