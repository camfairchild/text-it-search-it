import requests
from .helpers import google

def time_message(time_str: str) -> str:
    """Returns a message of the current time"""
    lat, long = google.get_location(time_str)
    time = google.get_time_by_lat_long(lat, long)
    return f"It is currently {time} in {time_str}"