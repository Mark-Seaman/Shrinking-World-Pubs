# Form Group

class StudentRequest(models.Model):

    # Course
    application_date = models.DateField(null=True, verbose_name=_("Today's Date"))
    course_of_interest = models.CharField(max_length=100, null=True, verbose_name=_('Course of Interest'))
    country = models.CharField(max_length=50, null=True, verbose_name=_('Country of Residence'))

    # Identification
    first_name = models.CharField(max_length=100, null=True, verbose_name=_('First Name'))
    first_last_name = models.CharField(max_length=100, null=True, verbose_name=_('First Last Name'))
    second_last_name = models.CharField(max_length=100, null=True, verbose_name=_('Second Last Name'))
    gov_id_number = models.CharField(max_length=20, null=True, verbose_name=_('Government ID Number'))
    id_type = models.CharField(max_length=20, null=True, verbose_name=_('ID Type'))
    birth_date = models.CharField(max_length=10, null=True, verbose_name=_('Birth Date'))

    # Education
    education = models.CharField( max_length=20, choices=EDUCATION_CHOICES, default='primary', verbose_name=_('Educational History') )
    school = models.CharField(max_length=200, null=True, verbose_name=_('Degree School'))
    programs_of_interest = models.CharField( max_length=20, choices=PROGRAM_CHOICES, null=True, verbose_name=_('I request admission to the follow study program') )

templates/edit.html

    {% extends 'theme.html' %}

    {% block content %}
    {% load crispy_forms_tags %}
    <form action="" method="post">{% csrf_token %}
        {{ form|crispy }}
    </form>
    {% endblock content %}

Can I display this form with 3 sections of controls: Course, Indentification, Education?

