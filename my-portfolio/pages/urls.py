# pages/urls.py

from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home_page, name="home-page"),
    path("pages/about-me/", views.about_me, name="about-me"),
    path("pages/contact/", views.contact_me, name="contact"),
]
