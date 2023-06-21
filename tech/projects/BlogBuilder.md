# Blog Builder

General Document Display Platform

[Dev Plan](Index)


## Overview

Blog Builder is a web application that displays content authored by markdown.


## Testing Tools

* Django Tests
* Probe Tests
* Web Page Tests
* User Tests


## Blog Hosting

Hammer is a web app platform that is used as the substrate for all of the
web apps authored by Shrinking World Solutions.

Hammer is deployed and running as a Droplet at Digital Ocean.

This single Droplet runs all of the following domains.

* [MarkSeaman.info](https://MarkSeaman.info) - Mark Seaman Private pages
* [shrinking-world.com](https://shrinking-world.com) - Shrinking World Solutions
* [spiritual-things.org](https://spiritual-things.org) - Spiritual Things
* [MarkSeaman.org](https://MarkSeaman.org) - Mark Seaman Public pages
* [seamansguide.com](https://seamansguide.com) - Seaman's Guide
* [seamanslog.com](https://seamanslog.com) - Seaman's Log
* [seamanfamily.org](https://seamanfamily.org) - Seaman Family


## Blog Page Loader

This general purpose tool displays documents identified by a requested URL.

urls.py

    from django.urls import path

    from .views_blog import BlogTodayView, BlogView

    urlpatterns = [

        path('<str:blog>', BlogView.as_view(), name='blog'),
        path('<str:blog>/<str:notebook>', BlogView.as_view(), name='blog_notebook'),
        path('<str:blog>/<str:notebook>/<str:article>', BlogView.as_view(), name='blog_article'),

    ]



## Application Platforms

Each of these platforms is built into the Hammer App that is hosted at 
Digital Ocean.

* App Builder - Applications developers
* Blog Builder - Page Loader
* Book Builder - Book Import, Edit, Export
* Course Builder - Course Import, Edit, Export


## Fixes and Issues

