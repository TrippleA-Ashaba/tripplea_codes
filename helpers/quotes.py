import random

QUOTES = (
    {
        "author": "Maya Angelou",
        "quote": "You can't use up creativity. The more you use, the more you have.",
    },
    {
        "author": "Eric Raymond",
        "quote": "Good programmers know what to write, Great ones know what to rewrite (and reuse)",
    },
    {
        "author": "Albert Einstein",
        "quote": "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.",
    },
    {
        "author": "George Eliot",
        "quote": "It is never too late to be what you might have been.",
    },
    {
        "author": "Douglas Adams",
        "quote": "I may not have gone where I intended to go, but I think I have ended up where I needed to be.",
    },
    {
        "author": "Frederick Brooks",
        "quote": "The hardest single part of building a software system is deciding precisely what to build.",
    },
    {
        "author": "NATO summit 1968 - the software crisis",
        "quote": "We build systems like the Wright brothers built airplanes—build the whole thing, push it off the cliff, let it crash, and start over again.",
    },
    {
        "author": "Donald Knuth",
        "quote": "Beware of bugs in the above code; I have only proved it correct, not tried it.",
    },
)


def get_quote():
    """
    Return a random quote from a list of dictionaries
    {
    'author':'string',
    'quote':'string'
    }

    """

    quote = random.choice(QUOTES)
    author = quote["author"]
    say = quote["quote"]
    return author, say
