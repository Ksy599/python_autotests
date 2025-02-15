import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2812b2005ca8a57f9fa86c14df013c7d'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '17277'
LEVEL = '1'


def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID, 'level': LEVEL})
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get(url = f'{URL}/me', headers = HEADER, params = {'trainer_id': TRAINER_ID})    
    assert response_get.json()["data"][0]["trainer_name"] == 'Лея' 
    