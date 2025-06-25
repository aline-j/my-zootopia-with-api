import json


def load_data(file_path):
    """
    Loads a JSON file
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    name = animal_obj.get('name')
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


def get_animal_data(animals_data):
    """
    Formats all animals into a single HTML string.
    """
    output = ''
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


# Main execution
animals_data = load_data('animals_data.json')
output = get_animal_data(animals_data)

# Read the HTML template
with open('animals_template.html', 'r') as htmlfile:
    template = htmlfile.read()

# Replace placeholder with animal info
final_html = template.replace('__REPLACE_ANIMALS_INFO__', output)

# Write the final HTML
with open('animals.html', 'w') as newhtmlfile:
    newhtmlfile.write(final_html)
