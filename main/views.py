from django.shortcuts import render
from helpers.blog import get_blogs
from helpers.quotes import get_quote


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    full_quote = get_quote()
    return render(
        request, "about.html", {"author": full_quote[0], "quote": full_quote[1]}
    )


def blog(request):
    blogs = get_blogs()
    return render(request, "blog.html", {"blogs": blogs})
