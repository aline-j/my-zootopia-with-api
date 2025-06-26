import requests
import os
from dotenv import load_dotenv

# load .env file
load_dotenv()

API_KEY = os.getenv("API_NINJAS_KEY")
URL = 'https://api.api-ninjas.com/v1/animals?name='
HEADERS = {'X-Api-Key': API_KEY}


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
    },
    """
    request_url = f'{URL}{animal_name}'
    response = requests.get(request_url, headers=HEADERS)
    animal_obj = response.json()
    return animal_obj
