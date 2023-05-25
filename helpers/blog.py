import requests


def get_blogs():
    r = requests.get(
        "https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@albertashaba.a"
    )
    data = r.json()
    blogs = data["items"]
    return blogs
