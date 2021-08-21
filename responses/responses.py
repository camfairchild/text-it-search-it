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

import asyncio

async def get_response(body: str) -> str:
    if (body[0] == '!') or (body[0] == '/'):
        body = body[1:]
        if (body.startswith('help')):
            return help_message()
        elif (body.startswith('weather')):
            return weather_message(body[7:])
        elif (body.startswith('news')):
            return news_message(body[4:])
        elif (body.startswith('translate')):
            return translate_message(body[9:])
        elif (body.startswith('joke')):
            return await joke_message()
        elif (body.startswith('time')):
            return time_message(body[4:])
        elif (body.startswith('date')):
            return date_message(body[4:])
        elif (body.startswith('directions')):
            return directions_message(body[10:])
        else:
            return error_message()
    else:
        return search_message(body)

