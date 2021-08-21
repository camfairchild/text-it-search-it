from jokeapi import Jokes

import asyncio

async def joke_message() -> str:
    j = await Jokes()
    joke = await j.get_joke(response_format="txt")
    
    return joke