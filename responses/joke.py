from jokeapi import Jokes

def joke_message() -> str:
    j = Jokes()
    joke = j.get_joke(response_format="txt")
    return joke