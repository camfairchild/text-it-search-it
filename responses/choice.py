from .helpers.db import get_user
from .error import error_message
from .news import get_article
from .search import get_search

def get_choice(conn, phone_number: str, choice: str) -> str:
    """
    Gets the chosen link from the database.
    """
    choice = int(choice)
    usr = get_user(conn, phone_number)
    if usr is not None:
        link = usr[1][choice]
        t = usr[2]
        if t == 'news':
            return get_article(link)
        else:
            return get_search(link)
    else:
        return error_message()
