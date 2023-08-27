# View Code

Perform the following text substitutions

    CoursePeriod  -->  Professor
    /period  -->  /professor
    Course Schedule  --> Professor


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

register/urls.py

    from django.urls import include, path
    from django.views.generic import TemplateView

    from .views_period import (
        PeriodListView,
        PeriodDetailView,
        PeriodCreateView,
        PeriodUpdateView,
        PeriodDeleteView,
    )

    urlpatterns = [
        # Period
        path('period/',                     PeriodListView.as_view(),   name='period-list'),
        path('period/<int:pk>',             PeriodDetailView.as_view(), name='period-detail'),
        path('period/add',                  PeriodCreateView.as_view(), name='period-add'),
        path('period/<int:pk>/',            PeriodUpdateView.as_view(), name='period-edit'),
        path('period/<int:pk>/delete',      PeriodDeleteView.as_view(), name='period-delete'),
    ]

