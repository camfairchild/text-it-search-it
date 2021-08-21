import requests
from .helpers import google

def time_message(query_str: str) -> str:
    """Returns a message of the current time"""
    coords = google.get_location(query_str)
    time = google.get_time_by_lat_long(coords)
    time_str =  time.strftime('%I:%M:%S %p')
    return f"It is currently {time_str} in {query_str}"