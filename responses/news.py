import requests, os

def get_news() -> str:
    """Return the news."""
    url = "https://api.nytimes.com/svc/topstories/v2/world.json"
    parms = {
        "api-key": os.getenv("NYTIMES_API_KEY")
    }
    response = requests.get(url, params=parms)
    results = response.json()['results']
    headlines = ""
    for i in range((min(5, int(response.json()["num_results"])))):
        title = results[i]["title"]
        headlines += (f"[{i}] {title}\n")
    # TODO: save state of user and respond with news article after choice
    return headlines

def news_message(news_str: str) -> str:
    """Return a message about the news."""

    return get_news()