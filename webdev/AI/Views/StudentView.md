Sure, here is an example of how you can create a TemplateView in Django to show the student details:

1. Create a template for the student details:
   - Create a file named `student_detail.html` in your templates directory.
   - Add the following code to the `student_detail.html` file:

   ```html
   <h1>Student Details</h1>
   <p>Name: {{ student.name }}</p>
   <p>Course: {{ student.course }}</p>
   <p>Github: <a href="{{ student.github }}">{{ student.github }}</a></p>
   <p>Server: <a href="{{ student.server }}">{{ student.server }}</a></p>
   ```

2. Create a view for the student details:
   - In your views.py file, add the following code:

   ```python
   from django.views.generic import TemplateView
   from .models import Student

   class StudentDetailView(TemplateView):
       template_name = 'student_detail.html'

       def get_context_data(self, **kwargs):
           context = super().get_context_data(**kwargs)
           student_id = self.kwargs['student_id']  # assuming you have a student_id parameter in your URL
           student = Student.objects.get(id=student_id)
           context['student'] = student
           return context
   ```

3. Define the URL for the student details view:
   - In your urls.py file, add the following code:

   ```python
   from django.urls import path
   from .views import StudentDetailView

   urlpatterns = [
       path('student/<int:student_id>/', StudentDetailView.as_view(), name='student_detail'),
   ]
   ```

With these steps, you have created a TemplateView called `StudentDetailView` that will render the `student_detail.html` template with the student details based on the `student_id` parameter in the URL. You can access the student details by using `{{ student.name }}`, `{{ student.course }}`, `{{ student.github }}`, and `{{ student.server }}` in your template.

When you visit the URL like `/student/1/`, it will show the details of the student with the ID 1.

Note: Don't forget to import the necessary modules/models in your files.