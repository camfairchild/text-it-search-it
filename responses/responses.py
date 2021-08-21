from .help import help_message
from .weather import weather_message
from .news import news_message
from .translate import translate_message
from .joke import joke_message
from .time import time_message
from .date import date_message
from .directions import directions_message
from .error import error_message
from .search import search_message

def get_response(body: str) -> str:
    if (body.startswith('!')):
        body = body[1:]
        if (body == 'help'):
            return help_message()
        elif (body == 'weather'):
            return weather_message(body[7:])
        elif (body == 'news'):
            return news_message(body[4:])
        elif (body == 'translate'):
            return translate_message(body[9:])
        elif (body == 'joke'):
            return joke_message()
        elif (body == 'time'):
            return time_message()
        elif (body == 'date'):
            return date_message()
        elif (body == 'directions'):
            return directions_message(body[10:])
        else:
            return error_message()
    else:
        return search_message(body)

