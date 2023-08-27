Consider this Django data model:

class CoursePeriod(models.Model):
    name = models.CharField(max_length=20, default="Fall 2023", verbose_name=_("Course Period Name"))
    start_date = models.DateField(null=True, verbose_name=_("Course Start Date"))
    end_date = models.DateField(null=True, verbose_name=_("Course End Date"))
    enrollment_open = models.DateField(null=True, verbose_name=_("Enrollment Open"))
    enrollment_closed = models.DateField(null=True, verbose_name=_("Enrollment Closed"))
    payment_due = models.DateField(null=True, verbose_name=_("Payment Due"))

Consider this import for CoursePeriod:

def import_course_periods(file_path):
    df = pd.read_csv(file_path)
    date_columns = ['start_date', 'end_date', 'enrollment_open', 'enrollment_closed', 'payment_due']
    df[date_columns] = df[date_columns].apply(pd.to_datetime)
    for _, row in df.iterrows():
        course_period = CoursePeriod(
            name=row['name'],
            start_date=row['start_date'].date(),
            end_date=row['end_date'].date(),
            enrollment_open=row['enrollment_open'].date(),
            enrollment_closed=row['enrollment_closed'].date(),
            payment_due=row['payment_due'].date(),
        )
        course_period.save()
    print("CoursePeriod records imported successfully.")

Rewrite this function to use the Meta fields to make this a generic import function.

---

Create a Django View to do a file upload to the Media directory

    from django.views.generic.edit import FormView
    from django.core.files.storage import FileSystemStorage

    class FileUploadView(FormView):
        template_name = 'upload.html'
        form_class = YourUploadForm  # Replace with your custom form class
        success_url = '/upload/success/'  # Replace with your desired success URL

        def form_valid(self, form):
            uploaded_file = form.cleaned_data['file']
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)
            return super().form_valid(form)


    <h1>Upload File</h1>
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Upload</button>
    </form>

