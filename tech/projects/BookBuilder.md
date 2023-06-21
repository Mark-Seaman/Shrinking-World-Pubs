# Book Builder

General Document Display Platform

[Dev Plan](Index)


## Overview

Book Builder is a web application that displays content authored by markdown.


## Book Hosting

Hammer is a web app platform that is used as the substrate for all of the
web apps authored by Shrinking World Solutions.

Hammer is deployed and running as a Droplet at Digital Ocean.

This single Droplet runs all of the following domains.

* [Seaman Guides](https://seamansguide.com/book/)
    * The Leverage Principle
    * A Seaman's Poems
    * A Seaman's Journey
    * A Seaman's Quest


## Book Objects

models.py

    # --------------------
    # Book
    #
    # title - title of the book
    # author - name of author
    # description - summary of the book

    class Book(models.Model):
        title = models.CharField(max_length=200)
        subtitle = models.CharField(max_length=200, null=True, blank=True)
        author = models.ForeignKey(Author, on_delete=models.CASCADE, editable=False)
        description = models.TextField(default='None')
        doc_path = models.CharField(max_length=200, default='Documents')

    # --------------------
    # Chapter
    #
    # book - points to book object
    # order - chapter order
    # title - title text of chapter
    # markdown - markdown text
    # html - HTML text from markdown
    # document - path to markdown file

    class Chapter(models.Model):
        book = models.ForeignKey(Book, on_delete=models.CASCADE, editable=False)
        order = models.IntegerField()
        title = models.CharField(max_length=200)
        markdown = models.TextField()
        html = models.TextField()
        document = models.CharField(max_length=200)


## Book URLs

This general purpose tool displays documents identified by a requested URL.

urls.py

    from django.urls import path

    from .views_book import *
    from .views_chapter import *

    urlpatterns = [

        # Book
        path('book',                        BookView.as_view(),        name='book_theme'),
        path('book/',                       BookListView.as_view(),    name='book_list'),
        path('book/<int:pk>',               BookDetailView.as_view(),  name='book_detail'),
        path('book/add',                    BookCreateView.as_view(),  name='book_add'),
        path('book/<int:pk>/',              BookUpdateView.as_view(),  name='book_edit'),
        path('book/<int:pk>/delete',        BookDeleteView.as_view(),  name='book_delete'),

        # Chapter
        path('chapter/',                    ChapterListView.as_view(),    name='chapter_list'),
        path('chapter/<int:pk>',            ChapterDetailView.as_view(),  name='chapter_detail'),
        path('chapter/add',                 ChapterCreateView.as_view(),  name='chapter_add'),
        path('chapter/<int:pk>/',           ChapterUpdateView.as_view(),  name='chapter_edit'),
        path('chapter/<int:pk>/delete',     ChapterDeleteView.as_view(),  name='chapter_delete'),

    ] 

## Book Views


## Book Import



## Book Export


## Testing

* Django Tests
* Probe Tests
* Web Page Tests
* User Tests


## Fixes and Issues

## Features Implemented


## Features To Implement



## Refactor and Simplify



