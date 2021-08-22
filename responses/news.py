import requests, os
from .helpers.db import set_user
from .helpers.parse import just_the_text


def get_news(conn, phone_number: str) -> str:
    """Return the news."""
    url = "https://api.nytimes.com/svc/topstories/v2/world.json"
    parms = {
        "api-key": os.getenv("NYTIMES_API_KEY")
    }
    response = requests.get(url, params=parms)
    results = response.json()['results']
    headlines = ""
    links = []
    for i in range((min(5, int(response.json()["num_results"])))):
        title = results[i]["title"]
        headlines += (f"[{i}] {title}\n")
        links.append(results[i]["url"])
    set_user(conn, phone_number, links, "news")
    return headlines

def news_message(conn, phone_number: str, news_str: str) -> str:
    """Return a message about the news."""
    
    return get_news(conn, phone_number)

def get_article(link: str) -> str:
    """Return the article from the link."""
    page = requests.get(link).text.encode("utf-8")
    return just_the_text(page)