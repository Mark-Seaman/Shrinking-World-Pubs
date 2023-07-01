# App Builder 

Software Development Tools Platform

[Dev Plan](Index)


## Overview

App Builder Workshop is a web application that aids applications developers


## Testing Tools

* Django Tests
* Probe Tests
* Web Page Tests
* User Tests


## Web Hosting

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


## Code Generator

To create a new data model an app developer first defines a data model class
in Python.

For example:

    class Document(models.Model):

        title = models.CharField(max_length=100)
        body = models.TextField()
        html = models.TextField(null=True)
        file = models.CharField(max_length=200, default='Index', unique=True)

Then a new data type object is created within the workshop.  These settings
are then used to create the code for the templates, urls, and views that 
support the new data model.


## Application Platforms

Each of these platforms is built into the Hammer App that is hosted at 
Digital Ocean.

* App Builder - Applications developers
* Blog Builder - Page Loader
* Book Builder - Book Import, Edit, Export
* Course Builder - Course Import, Edit, Export


## Fixes and Issues

