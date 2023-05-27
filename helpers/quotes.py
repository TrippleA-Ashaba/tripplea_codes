import random

quotes = [
    {
        "author": "Maya Angelou",
        "quote": "You can't use up creativity. The more you use, the more you have.",
    },
]


def get_quote():
    quote = random.choice(quotes)
    author = quote["author"]
    say = quote["quote"]
    return author, say
