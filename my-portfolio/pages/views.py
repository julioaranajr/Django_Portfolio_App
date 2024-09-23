from django.shortcuts import render


def home_page(request):
    return render(request, "pages/home-page.html", {})

def about_me(request):
    return render(request, "pages/about-me.html", {})

def contact_me(request):
    return render(request, "pages/contact.html", {})
