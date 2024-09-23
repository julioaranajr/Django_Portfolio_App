# Django Portfolio App

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

This Portafolio App is a Django project that will help you to create a portfolio website. It will have a homepage, an about page, and a projects page. The projects page will list all the projects you have worked on, and each project will have its own detail page.

In this repository we are to:

1. Understand the Structure of a Django Website

2. Create the Example Portfolio Project With Django
   2.1 Set Up the Development Environment
   2.2 Start Your First Django Project

3. Add the Pages App
   3.1 Create a View
   3.2 Add a Route

4. Add Bootstrap to Your App

5. Add the Projects App
   5.1 Define a Model
   5.2 Dive Into the Django Shell
   5.3 Create the Views
   5.4 Craft the Templates
   5.5 Add the Routes
   5.6 Leverage the Django Admin Site
   5.7 Upload Images

6. Conclusion

---

## 1. Understand the Structure of a Django Website

Before we start building our portfolio app, let’s understand the structure of a Django website. A Django website is made up of one or more Django apps. Each app is a Python package that follows a certain convention. An app can be a blog, a forum, a photo gallery, or anything else you want it to be.

A Django project is a collection of settings for an instance of Django, including database configuration, Django-specific options, and application-specific settings. A project can contain multiple apps. An app can be in multiple projects.

A Django project is created using the `django-admin` command-line tool. A Django app is created using the `manage.py` command-line tool.

---

## 2. Create the Example Portfolio Project With Django

### 2.1 Set Up the Development Environment

To get started with Django, you need to have Python installed on your computer. You can download Python from the official website. Once you have Python installed, you can install Django using pip, the Python package manager.

Create a new virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install the dependencies for this project if you haven't installed them yet:

```bash
(venv)
python -m pip install -r requirements.txt
```

### 2.2 Start Your First Django Project

To create a new Django project, run the following command:

```bash
django-admin startproject portfolio
```

This will create a new directory called `portfolio` with the following structure:

```bash
portfolio/
    manage.py
    portfolio/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

The `manage.py` file is a command-line utility that lets you interact with your Django project. You can use it to run development servers, create new apps, and more.

The `portfolio` directory is the actual Python package for your project. It contains the settings for your project, the URL configurations, and the WSGI application.

To start the development server, run the following command:

```bash
python manage.py runserver
```

This will start the development server on `http://localhost:8000/`. You can visit this URL in your web browser to see the default Django welcome page.

---

## 3. Add the Pages App

### 3.1 Create a View

To create a new Django app, run the following command:

```bash
python manage.py startapp pages
```

This will create a new directory called `pages` with the following structure:

```bash
pages/
    migrations/
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
```

The `views.py` file is where you define the views for your app. A view is a Python function that takes a web request and returns a web response. You can use views to render HTML templates, redirect to other pages, and more.

Create a new view in the `views.py` file:

```python
from django.http import HttpResponse

def home_page(request):
    return HttpResponse('Home Page')
```

### 3.2 Add a Route

To add a route for the new view, open the `urls.py` file in the `portfolio` directory and add the following code:

```python
from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
]
```

This code imports the `home_page` view from the `pages` app and maps it to the root URL of the website. Now when you visit `http://localhost:8000/`, you should see the text "Home Page" displayed in your web browser.

---

## 4. Add Bootstrap to Your App

To add Bootstrap to your app, you need to download the Bootstrap CSS and JavaScript files and include them in your HTML templates. You can download Bootstrap from the official website or use a CDN to include it in your project.

Create a new directory called `static` in the `pages` app:

```bash
mkdir pages/static
```

Create a new directory called `css` in the `static` directory:

```bash
mkdir pages/static/css
```

Download the Bootstrap CSS file and save it in the `css` directory:

```bash
curl https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css -o pages/static/css/bootstrap.min.css
```

Create a new directory called `js` in the `static` directory:

```bash
mkdir pages/static/js
```

Download the Bootstrap JavaScript file and save it in the `js` directory:

```bash
curl https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js -o pages/static/js/bootstrap.min.js
```
