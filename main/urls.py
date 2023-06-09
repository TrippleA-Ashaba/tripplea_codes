from django.urls import path

from .views import home, about, blog

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("blog/", blog, name="blog"),
]
