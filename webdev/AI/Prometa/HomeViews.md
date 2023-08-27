Create Django Views for these URLs.

urls.py:

urlpatterns = [
    path('',                            PrometaUserView.as_view(),      name='home'),
    path("annon",                       StudentRequestView.as_view(),   name='request'),
    path("professor",                   ProfessorView.as_view(),        name='professor'),
    path("sysadmin",                    SysadminView.as_view(),         name='sysadmin'),
    path("registrar",                   RegistrarView.as_view(),        name='registrar'),
    path("student",                     StudentView.as_view(),          name='student'),
}

views.py:

class PrometaUserView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return reverse_lazy('request')
        if self.request.user.is_superuser:
            return reverse_lazy('sysadmin')
        return '/request'
           
class RequestView(TemplateView):
    template_name="request.html"


templates/request.html:

    {% extends "theme.html" %}
    {% load i18n %}

    {% block title %}Request{% endblock %}

    {% block content %}

    <h1>Request View</h1>

    {% endblock %}
