import datetime

def date_message() -> str:
    """Return a message about the date."""
    return "Today is " + str(datetime.date.today()) + "."