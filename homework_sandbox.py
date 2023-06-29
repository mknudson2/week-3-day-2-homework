from random import randint
from requests import get
from IPython.display import Image, display


random_pokemon = randint(1, 898)

class Pokemon:
    
    def __init__(self):
        self.name = str(randint(1, 898))
        self.image = ''
        self.evolves_to = None
    
    def poke_api_call(self):
        res = get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
        if res.ok:
            data = res.json()
            self.name = data['name']
            self.image = data['sprites']['versions']['generation-v']['black-white']['animated']['front_shiny']
            if not self.image:
                self.image = data['sprites']['front_default']
            species_url = data['species']['url']
            self.get_evolution_chain(species_url)
    
    def get_evolution_chain(self, species_url):
        res = get(species_url)
        if res.ok:
            data = res.json()
            evolution_chain_url = data['evolution_chain']['url']
            self.parse_evolution_chain(evolution_chain_url)
    
    def parse_evolution_chain(self, evolution_chain_url):
        res = get(evolution_chain_url)
        if res.ok:
            data = res.json()
            chain = data['chain']
            while chain:
                species_name = chain['species']['name']
                if species_name == self.name:
                    evolves_to = chain['evolves_to']
                    if evolves_to:
                        self.evolves_to = evolves_to[0]['species']['name']
                    break
                chain = chain['evolves_to'][0] if chain.get('evolves_to') else None
    
    def evolve(self):
        if self.evolves_to:
            self.name = self.evolves_to
            self.poke_api_call()
        else:
            print("This Pokémon cannot evolve.")
    
    def display_pokemon_info(self):
        self.display_pokemon_image()
        print(f'{self.name}')
        if self.evolves_to:
            choice = input("Do you want to evolve this Pokémon? (yes/no): ")
            if choice.lower() == "yes":
                self.evolve()
                self.display_pokemon_info()
    
    def display_pokemon_image(self, width=150):
        display(Image(self.image, width=width))
    

pokemon = Pokemon()
pokemon.poke_api_call()
pokemon.display_pokemon_info()