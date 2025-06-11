import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7ad7c8447790f057c277164024909fc9'
#pokemon_id = "275895"
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_createpokemon = {
    "name": "Слоупок",
    "photo_id": 79
}

response_createpokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_createpokemon)
print(response_createpokemon.status_code)
print(response_createpokemon.text)

pokemon_id = response_createpokemon.json()['id']
print(pokemon_id)

body_changepokemon = {
    "pokemon_id": pokemon_id,
    "name": "-                                                -",
    "photo_id": 79
}

response_changepokemon = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_changepokemon)
print(response_changepokemon.status_code)
print(response_changepokemon.text)

body_catchpokemon = {
    "pokemon_id": pokemon_id
}

response_catchpokemon = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catchpokemon)
print(response_catchpokemon.status_code)
print(response_catchpokemon.text)


