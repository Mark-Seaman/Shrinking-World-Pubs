I have a Django data model for a student object.

class Student(models.Model):
    user = models.ForeignKey(PrometaUser, on_delete=models.CASCADE, verbose_name=_("User"))
    name = models.CharField(max_length=100, null=True, verbose_name=_("Name"))
    country = models.CharField(max_length=50, null=True, verbose_name=_("Country"))
    email = models.EmailField(null=True, verbose_name=_("Email"))
    phone = models.CharField(max_length=20, null=True, verbose_name=_("Phone"))
    address = models.TextField(null=True, verbose_name=_("Address"))
    payment = models.BooleanField(null=True, verbose_name=_("Payment"))

I want to create a ListView that shows 'user__username' and 'name'.

The DetailView should show all of the fields.

Write the data model and views while using the existing templates. 


templates/list.html:

    {% for object in object_list %}
        {% for label, value in object.get_fields %}
            {{ value }}
        {% endfor %}
    {% endfor %}


templates/detail.html:

    <table class="table">
        <tr>
            {% for field in object.get_fields %}
            <th>{{ field.verbose_name }}</th>
            {% endfor %}
        </tr>

        {% for label, value in object.get_fields %}
        <tr>
            <td><b>{{ label }}</b></td>
            <td>{{ value }}<br><br></td>
        </tr>
        {% endfor %}

    </table>
