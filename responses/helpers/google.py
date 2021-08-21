from datetime import datetime, timedelta
from typing import Tuple
import requests
import os

def get_location(loc_str: str) -> Tuple[float, float]:
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {
        'address': loc_str,
        'key': os.getenv("GOOGLE_API_KEY")
    }
    r = requests.get(url, params=params)
    loc_json = r.json()
    loc_lat = loc_json['results'][0]['geometry']['location']['lat']
    loc_lng = loc_json['results'][0]['geometry']['location']['lng']
    return loc_lat, loc_lng

def get_time_by_lat_long(coords: Tuple[int, int]) -> datetime:
    """
    Returns the timezone in which the given coordinates are located.
    """
    url = 'https://maps.googleapis.com/maps/api/timezone/json'
    params = {
        'location': '{},{}'.format(coords[0], coords[1]),
        'timestamp':  datetime.now().strftime('%s'),
        'key': os.getenv("GOOGLE_API_KEY")
    }
    r = requests.get(url, params=params)
    rawOffset = r.json()['rawOffset']
    dstOffset = r.json()['dstOffset']
    offset = rawOffset + dstOffset
    time = datetime.utcnow() + timedelta(seconds=offset)
    return time
