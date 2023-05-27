import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("BLOG_API_KEY")


def get_blogs():
    """Return a list of Dictionary blog entries"""

    r = requests.get(
        f"https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@albertashaba.a&api_key={API_KEY}"
    )
    data = r.json().get("items")

    # exclude keys not used
    keys_to_exclude = {"link", "author", "description", "content", "enclosure"}

    # new list of blogs without unused keys
    blogs = [
        {k: v for k, v in blog.items() if k not in keys_to_exclude} for blog in data
    ]

    return blogs
