# Login With Email

Create a view and template to let users login with their email address.

    from django.contrib.auth.models import AbstractUser

    class PrometaUser(AbstractUser):
        is_registrar = models.BooleanField(default=False)
        is_student = models.BooleanField(default=False)
        is_professor = models.BooleanField(default=False)

templates/registration/login.html

    {% extends 'theme.html' %}
    {% block content %}
    <form method="post" class="m-5">
        {% csrf_token %}

        {{ form }}

        <button type="submit" class="btn btn-primary m-5">Log In</button>
    </form>
    {% endblock content %}

---

# Login Without View

Write a Django Unit Test  to demonstrate logging in.

