import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("BLOG_API_KEY")


def get_blogs():
    r = requests.get(
        f"https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@albertashaba.a&api_key={API_KEY}"
    )
    data = r.json()
    blogs = data["items"]
    return blogs
