import requests, os

def search_message(query_str: str) -> str:
    """Return a message that the search query was executed."""

    key = os.getenv('GOOGLE_API_KEY')
    engineID = "<57684878dbe99f18b>"
    page = 1
    start = (page - 1) * 10 + 1
    url = f"https://www.googleapis.com/customsearch/v1?key={key}&cx={engineID}&q={query_str}&start={start}"

    data = requests.get(url).json()

    search_items = data.get("items")

    resultStr = ""

    for i, search_item in enumerate(search_items, start=1):

        title = search_item.get("title")
        snippet = search_item.get("snippet")
        link = search_item.get("link")

        if (i == 1):
            f = open("urlList.txt", "w")
        else:
            f = open("urlList.txt", "a")

        f.write(link, "\n")

        resultStr = resultStr, "Title:", title, "\n", "Description:", snippet, "\n\n"

        f.close()

    return resultStr