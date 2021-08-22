import requests, os, html
from .helpers.parse import remove_html_tags

def get_directions(origin: str, destination: str) -> str:
    url = 'https://maps.googleapis.com/maps/api/directions/json'
    params = {
        'origin': origin,
        'destination': destination,
        'key': os.getenv('GOOGLE_API_KEY')
    }
    resp = requests.get(url=url, params=params)
    steps =  resp.json()["routes"][0]["legs"][0]["steps"]
    directions_str = ""
    for step in steps:
        directions_str += remove_html_tags(step["html_instructions"]) + "\n"
    print(directions_str)
    return directions_str

def directions_message(directions_str: str) -> str:
    """Return a message for the given directions."""
    locations = directions_str.split(' to ')
    origin = locations[0]
    destination = locations[1]

    return get_directions(origin, destination)