# Course Builder

General Document Display Platform

[Dev Plan](Index)


## Overview

Course Builder is a web application that displays content authored by markdown.


## Course Hosting

Hammer is a web app platform that is used as the substrate for all of the
web apps authored by Shrinking World Solutions.

Hammer is deployed and running as a Droplet at Digital Ocean.

This single Droplet runs all of the following domains.

* [Shrinking World Courses](https://shrinking-world.com/course)
    * UNC BACS 200 - Intro to Web Dev - Spring 2022
    * UNC BACS 350 - Intermediate Web Dev - Fall 2021
    * UNC CS 350 - Software Engineering - Fall 2020


## Course Objects

models.py

    # --------------------
    # Course
    #
    # name - identity of course
    # title - short description
    # description - summary of course content
    # author - teacher of course with permissions to modify content
    # doc_path - lookup for lesson and project documents
    # num_projects - weekly projects
    # num_lessons - total number of lessons
    # github_repo - directory of Github repo to pull

    class Course(models.Model):
        name = models.CharField(max_length=20, default='XXX')
        title = models.CharField(max_length=200)
        subtitle = models.CharField(max_length=200, null=True, blank=True)
        author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
        description = models.TextField(default='No Description is Set')
        doc_path = models.CharField(max_length=200, default='Documents')
        num_projects = models.IntegerField(default=14)
        num_lessons = models.IntegerField(default=42)
        github_repo = models.CharField(max_length=200, default='~/Github/UNC-BACS200-2022-Spring')

    # --------------------
    # Lesson
    #
    # course - points to course object
    # order - lesson number order
    # title - title text of chapter
    # date - due date for lesson
    # week - week of class
    # document - path to markdown file
    # url - page to load

    class Lesson(models.Model):
        course = models.ForeignKey(Course, on_delete=models.CASCADE, editable=False)
        order = models.IntegerField()
        title = models.CharField(max_length=200, default='No title')
        date = models.DateField(null=True)
        week = models.IntegerField(null=True)
        url_lecture = models.URLField(null=True, blank=True)

    # --------------------
    # Project
    #
    # course - points to course object
    # date - due date for lesson
    # title - title text of chapter
    # order - lesson number order
    # document - path to markdown file
    # url - page to load

    class Project(models.Model):
        course = models.ForeignKey(Course, on_delete=models.CASCADE)
        date = models.DateField(null=True)
        title = models.CharField(max_length=100, default='No title')
        order = models.IntegerField()
        page = models.CharField(max_length=100, default='index.html')


## Course URLs

This general purpose tool displays documents identified by a requested URL.

urls.py

    from django.conf import settings
    from django.conf.urls.static import static
    from django.urls import path

    from .views_course import *

    urlpatterns = [

        # Course
        path('course/', CourseListView.as_view(), name='course_list'),
        path('course/<int:pk>/', CourseUpdateView.as_view(), name='course_edit'),
        path('course/<int:pk>/import', CourseImportView.as_view(), name='course_import'),
        path('course/<str:course>', ContentView.as_view(), name='course_index'),

        # Lessons and Projects
        path('course/<str:course>/lesson/<int:order>', LessonView.as_view(), name='lesson'),
        path('course/<str:course>/slides/<int:order>', SlidesView.as_view(), name='slides'),
        path('course/<str:course>/project/<int:order>', ProjectView.as_view(), name='project'),
        path('course/<str:course>/docs/<str:doc>', CourseDocView.as_view()),

    ] 


## Course Views


## Authoring Course Content


## Course Import


## Course Export


## Testing

* Django Tests
* Probe Tests
* Web Page Tests
* User Tests


## Fixes and Issues

## Features Implemented


## Features To Implement



## Refactor and Simplify



