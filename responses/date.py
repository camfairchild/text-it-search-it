import datetime
from .helpers.google import get_location, get_time_by_lat_long

def date_message(date_str: str) -> str:
    """Return a message about the date."""
    # Get location
    location = get_location(date_str)
    # Get the current date
    date = get_time_by_lat_long(location)

    return f"The date in {location} is {date.strftime('%a %d %b')}."