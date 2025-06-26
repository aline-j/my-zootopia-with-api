import requests
import os
from dotenv import load_dotenv


# load .env file
load_dotenv()


API_KEY = os.getenv("API_NINJAS_KEY")
URL = 'https://api.api-ninjas.com/v1/animals?name='
HEADERS = {'X-Api-Key': API_KEY}


def load_data_from_api(name):
    """
    Get animal name from user input
    Loads animals data from Animals API from Ninja API
    """
    request_url = f'{URL}{name}'
    response = requests.get(request_url, headers=HEADERS)
    animal_obj = response.json()
    return animal_obj


def serialize_animal(animal_obj, name):
    info = {
        "Diet": animal_obj['characteristics'].get('diet'),
        "Location": animal_obj.get('locations')[0],
        "Type": animal_obj['characteristics'].get('type'),
        "Class": animal_obj['taxonomy'].get('class'),
        "Name of young": animal_obj['characteristics'].get('name_of_young'),
        "Lifespan": animal_obj['characteristics'].get('lifespan'),
        "Skin type": animal_obj['characteristics'].get('skin_type'),
        "Weight": animal_obj['characteristics'].get('weight'),
        "Height": animal_obj['characteristics'].get('height'),
        "Length": animal_obj['characteristics'].get('length')
    }

    output = '<li class="cards__item">\n'
    output += f'<div class="card__title">{name}</div>\n'
    output += '<div class="card__text">\n<ul>\n'

    for key, value in info.items():
        if value:
            output += f'<li><strong>{key}:</strong> {value}</li>\n'

    output += '</ul>\n</div>\n</li>\n'
    return output


def get_animal_data(animals_data, name):
    """
    Formats all animals into a single HTML string.
    """
    if animals_data:
        output = ''
        for animal in animals_data:
            output += serialize_animal(animal, name)
        print('Website was successfully generated to the file animals.html.')
        return output
    else:
        return f'<h2 style="text-align: center; margin-top: 100px;">The animal "{name}" does not exist.</h2>'


# Main execution
name = input('Enter animal name: ')
animals_data = load_data_from_api(name)
output = get_animal_data(animals_data, name)

# Read the HTML template
with open('animals_template.html', 'r') as htmlfile:
    template = htmlfile.read()

# Replace placeholder with animal info
final_html = template.replace('__REPLACE_ANIMALS_INFO__', output)

# Write the final HTML
with open('animals.html', 'w') as newhtmlfile:
    newhtmlfile.write(final_html)
