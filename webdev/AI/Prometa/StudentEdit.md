Given this Django code

    class Student(models.Model):
        user = models.ForeignKey(PrometaUser, on_delete=models.CASCADE, null=True, editable=False, verbose_name=_("User"))
        name = models.CharField(max_length=100, null=True, verbose_name=_("Name"))
        country = models.CharField(max_length=50, null=True, verbose_name=_("Country"))
        phone = models.CharField(max_length=20, null=True, verbose_name=_("Phone"))
        address = models.TextField(null=True, verbose_name=_("Address"))
        payment = models.BooleanField(null=True, verbose_name=_("Payment"))


    class StudentEditView(CreateView):
        model = StudentRequest
        template_name = 'edit.html'
        fields = '__all__'
        success_url = reverse_lazy('request_list') 


    {% extends 'theme.html' %}
    {% load i18n %}
    {% block content %}
    <h1>EDIT REQUEST</h1>
    {% load crispy_forms_tags %}
    <form action="" method="post">{% csrf_token %}
        {{ form|crispy }}
        <button class="btn m-5" type="submit">
            {% translate "Save Record" %}
        </button>
    </form>
    {% endblock content %}

Create code to edit the records.   If student name is "Registrar" then hide the payment field in the template. 



