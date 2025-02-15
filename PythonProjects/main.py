import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2812b2005ca8a57f9fa86c14df013c7d'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}


body_pokemons = {
    "name": "Бомбикс",
    "photo_id": 1
}

body_pokemons_put = {
    "pokemon_id": "234496",
    "name": "Бульбазавр",
    "photo_id": 1
}

body_app_pokeball = {
    "pokemon_id": "234476"
}


response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(response.text)

response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons_put)
print(response_put.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_app_pokeball)
print(response_add_pokeball.text)


