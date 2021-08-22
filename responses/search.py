import requests, os
from .helpers.db import set_user
from .helpers.parse import just_the_text

def search_message(conn, phone_number: str, query_str: str) -> str:
    """Return a message that the search query was executed."""

    key = os.getenv('GOOGLE_API_KEY')
    engineID = "dd6211de40a215054"
    url = "https://customsearch.googleapis.com/customsearch/v1"
    params = {
        "key": key,
        "cx": engineID,
        "q": query_str,
    }

    data = requests.get(url, params=params).json()
    print(data)

    search_items = data["items"][:5]

    resultStr = ""
    options = []
    for i, search_item in enumerate(search_items, start=1):

        title = search_item.get("title")
        snippet = search_item.get("snippet")
        link = search_item.get("link")

        resultStr += f"[{i}] Title: {title}\nDescription: {snippet}\n\n"

        options.append(link)
    set_user(conn, phone_number, options, "search")

    return resultStr

def get_search(link: str) -> str:
    """Return further results from the search"""
    page = requests.get(link).text.encode("utf-8")
    return just_the_text(page)
