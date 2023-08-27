Given these data models

    class PrometaUser(AbstractUser):
        name = models.CharField(max_length=200, default="None", null=True)
        is_registrar = models.BooleanField(default=False)
        is_student = models.BooleanField(default=False)
        is_professor = models.BooleanField(default=False)

Create code to export the records from the database to a CSV file (data/students.csv) 

    class PrometaUserListView(ListView):
        template_name = 'list2.html'
        model = PrometaUser
        context_object_name = 'users'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            fields = ['username', 'email']
            context['title'] = f'List of {self.model._meta.verbose_name_plural.title()}'
            context['data'] = PrometaUser.objects.values(*fields)
            return context

Write template code to show the table.

    <h1>{{ title }}</h1>
    <table>
        <thead>
            <tr>
                {% for field in data.0 %}
                <th>{{ field }}</th>
                {% endfor %}
            </tr>
        </thead>
        <tbody>
            {% for row in data %}
            <tr>
                {% for value in row.values %}
                <td>{{ value }}</td>
                {% endfor %}
            </tr>
            {% endfor %}
        </tbody>
    </table>

Is this code enough to get the file downloaded?


from django.http import FileResponse

def download_file(request):
    file_path = 'data/users.csv'
    with open(file_path, 'rb') as f:
        response = FileResponse(f)
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_path)
    return response

urlpatterns = [
    path('user/download',               download_file),
]

Create a generic Django View that downloads the file "data/users.csv" and then confirms the download by showing a success page.

