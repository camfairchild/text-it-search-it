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
from .choice import get_choice

import asyncio, re

async def get_response(body: str, phone_number: str=None, conn=None) -> str:
    if (body[0].isdigit()):
        return get_choice(conn, phone_number, int(body[0]))
    elif (body[0] == '!') or (body[0] == '/'):
        body = body[1:]
        if (bool(re.match('help', body, re.I))):
            return help_message()
        elif (bool(re.match('weather', body, re.I))):
            return weather_message(body[7:])
        elif (bool(re.match('news', body, re.I))):
            return news_message(conn, phone_number, body[5:])
        elif (bool(re.match('translate', body, re.I))):
            return translate_message(body[10:])
        elif (bool(re.match('joke', body, re.I))):
            return await joke_message()
        elif (bool(re.match('time', body, re.I))):
            return time_message(body[5:])
        elif (bool(re.match('date', body, re.I))):
            return date_message(body[5:])
        elif (bool(re.match('directions', body, re.I))):
            return directions_message(body[11:])
        else:
            return error_message()
    else:
        return search_message(conn, phone_number, body)

