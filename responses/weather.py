from typing import Tuple
from .helpers.google import get_location
import os, requests

def get_weather(location: Tuple[float, float]) -> str:
    url = "http://api.weatherbit.io/v2.0/current"
    params = {
        "key": os.getenv("WEATHER_BIT_KEY"),
        "lat": location[0],
        "lon": location[1],
    }
    response = requests.get(url, params=params)
    return response.json()["data"][0]["weather"]["description"]

def weather_message(weather_str: str) -> str:
    """
    Return a string containing the weather.
    """
    coords = get_location(weather_str)
    weather = get_weather(coords)
    return f"{weather} today in {weather_str}"