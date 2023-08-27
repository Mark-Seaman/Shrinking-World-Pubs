# View Code

Consider this Django Data Model.

## Data Model

register/models.py

    class CoursePeriod(models.Model):
        start_date = models.DateField(verbose_name=_("Course Start Date"))
        end_date = models.DateField(verbose_name=_("Course End Date"))

        def get_fields(self):
            return [(field.verbose_name, getattr(self, field.name)) for field in self._meta.fields]

        def detail_link(self):
            return button_html(f'/period/{self.pk}', 'View Record')

        def delete_link(self):
            return button_html(f'/period/{self.pk}/delete', 'Delete Record')

        def edit_link(self):
            return button_html(f'/period/{self.pk}/', 'Edit Record')

        @classmethod
        def get_model_label(cls):
            return cls._meta.verbose_name_plural
        
        class Meta:
            verbose_name = "Course Schedule"
            verbose_name_plural = "Course Schedule"


## HTML Template

templates/list.html

    <table class="table table-hover">
        <tr>
            {% for label, _ in object_list.0.get_fields %}
            <th>{{ label }}</th>
            {% endfor %}
            <th>Actions</th>
        </tr>

        {% for object in object_list %}
        <tr>
            {% for label, value in object.get_fields %}
            <td>{{ value }}</td>
            {% endfor %}
            <td>{% autoescape off %}{{ object.detail_link }}{% endautoescape %}</td>
        </tr>
        {% endfor %}

    </table>

    {% autoescape off %}{{ add_button }}{% endautoescape %}
    {% autoescape off %}{{ list_button }}{% endautoescape %}


register/views.py

    class PeriodListView(ListView):
        model = CoursePeriod
        template_name = 'list.html'

        def get_context_data(self, **kwargs):
            kwargs = super().get_context_data(**kwargs)
            model_label = self.model.get_model_label()
            data = {
                'title': f'List of {model_label}',
                'add_button': button_html("/period/add", f'Add {model_label}' ),
                'list_button': button_html('/period/', f'{model_label} List'),
            }
            kwargs.update(data)
            return kwargs

## URLS


## Generate New Views

Consider this new data model:

    class Professor(models.Model):
        user = models.ForeignKey(PrometaUser, on_delete=models.CASCADE, editable=False, verbose_name=_("User"))
        address = models.TextField(null=True, verbose_name=_("Address"))
        phone = models.CharField(max_length=100, null=True, verbose_name=_("Phone"))

Build a list view and URLs with a base prefix of '/professor' and a restful API.


## Refactor

Your task is to refactor this code to make it simpler while eliminating duplicate and unused code.

Present the list view with an edit button for each record, and add and list buttons for the whole data type.

Use the data type label from the data model to set the text on the buttons.


