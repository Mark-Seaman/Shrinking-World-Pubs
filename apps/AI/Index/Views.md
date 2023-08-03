# Views

In Django, views are Python functions or classes that define the logic behind a specific web page or a group of related web pages. They handle the request made by the user and return a response, which can be an HTML page, a JSON object, or any other kind of data.

## Function-based views

Function-based views are the simplest way to define views in Django. They are Python functions that take a request object as a parameter and return a response object. 

Here's a basic example of a function-based view:

```python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")
```

In this example, the `hello_world` function takes a `request` object as a parameter and returns an `HttpResponse` object with the content "Hello, World!". This view can be mapped to a URL so that when a user visits that URL, this function is called and the response is sent back to the user.

## Class-based views

Class-based views are another way to define views in Django. They are Python classes that inherit from a base view class provided by Django. Class-based views offer more flexibility and allow for code reuse through inheritance.

Here's an example of a class-based view:

```python
from django.views import View
from django.http import HttpResponse

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello, World!")
```

In this example, the `HelloWorldView` class inherits from the `View` base class provided by Django. It defines a `get` method that takes a `request` object as a parameter and returns an `HttpResponse` object with the content "Hello, World!". Similar to the function-based view, this class-based view can also be mapped to a URL.

## URL mapping

To connect views to URLs, you need to define URL patterns in your Django project's URLs configuration. The URLs configuration maps specific URLs to their corresponding views.

Here's an example of URL mapping using the `path` function:

```python
from django.urls import path
from .views import hello_world, HelloWorldView

urlpatterns = [
    path('hello/', hello_world),
    path('class_hello/', HelloWorldView.as_view()),
]
```

In this example, the URL '/hello/' is mapped to the `hello_world` function-based view, while '/class_hello/' is mapped to the `HelloWorldView` class-based view.

## Conclusion

Views in Django are responsible for handling user requests and returning appropriate responses. They can be defined as simple function-based views or more flexible class-based views. URL mapping connects specific URLs to their corresponding views.