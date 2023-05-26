from django.shortcuts import render
from helpers.blog import get_blogs


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def blog(request):
    blogs = get_blogs()
    return render(request, "blog.html", {"blogs": blogs})
