# View Error Handling

Add error handling to this view.

class StudentRequestCreateView(CreateView):
    model = StudentRequest
    template_name = 'application.html'
    form_class = ApplicationForm
    success_url = '/request/thank_you'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['title'] = 'Student Application Form'
        return kwargs

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['application_date'].widget = HiddenInput()
        if not self.request.user.is_authenticated:
            form.fields['payment'].widget = HiddenInput()
            form.fields['status'].widget = HiddenInput()
            form.fields['status_reason'].widget = HiddenInput()
        return form

templates/application.html

{% extends 'theme.html' %}


{% block navbar %}
{% endblock navbar %}


{% block content %}
{% load crispy_forms_tags %}

<form action="" method="post">{% csrf_token %}

    {{ form.application_date|as_crispy_field }}

    {{ form.first_name|as_crispy_field }}
    {{ form.first_last_name|as_crispy_field }}
    {{ form.second_last_name|as_crispy_field }}
    {{ form.gov_id_number|as_crispy_field }}
    {{ form.id_type|as_crispy_field }}
    {{ form.birth_date|as_crispy_field }}
    {{ form.country|as_crispy_field }}


    <button type="submit" class="btn">Submit</button>
</form>

{% endblock content %}


class StudentRequest(models.Model):

    # Course
    application_date = models.DateField(
        null=True, verbose_name=_("Today's Date"))
    course_of_interest = models.CharField(
        max_length=100, null=True, verbose_name=_('Course of Interest'))
    # country = models.CharField(max_length=50, null=True,)
    country = CountryField(null=True, verbose_name=_('Country of Residence'))

    # ID
    first_name = models.CharField(
        max_length=100, null=True, verbose_name=_('First Name'))
    first_last_name = models.CharField(
        max_length=100, null=True, verbose_name=_('First Last Name'))
    second_last_name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_('Second Last Name'))

 