Given this data model

    class Student(models.Model):
        user = models.ForeignKey(PrometaUser, on_delete=models.CASCADE, null=True, editable=False, verbose_name=_("User"))
        name = models.CharField(max_length=100, null=True, verbose_name=_("Name"))
        country = models.CharField(max_length=50, null=True, verbose_name=_("Country"))
        email = models.EmailField(null=True, verbose_name=_("Email"))
        phone = models.CharField(max_length=20, null=True, verbose_name=_("Phone"))
        address = models.TextField(null=True, verbose_name=_("Address"))
        payment = models.BooleanField(null=True, verbose_name=_("Payment"))

With this sample data

data/student.csv

    user,name,country,email,phone,address,payment
    liamanderson@example.com,,Mexico,none@nowhere.org,7230453301,liamanderson@example.com,False
    williamsmith@example.com,,Colombia,none@nowhere.org,0607348918,williamsmith@example.com,False
    liamtaylor@example.com,,Spain,none@nowhere.org,1651721173,liamtaylor@example.com,False
    emmamartinez@example.com,,Argentina,none@nowhere.org,7007193895,emmamartinez@example.com,False
    liamjones@example.com,,Peru,none@nowhere.org,8958209947,liamjones@example.com,False
    williamrodriguez@example.com,,Venezuela,none@nowhere.org,3363079825,williamrodriguez@example.com,False
    williammartinez@example.com,,Chile,none@nowhere.org,5658635033,williammartinez@example.com,False
    lucastaylor@example.com,,Ecuador,none@nowhere.org,2466036450,lucastaylor@example.com,False
    harperwright@example.com,,Guatemala,none@nowhere.org,7160663774,harperwright@example.com,False
    harpergarcia@example.com,,Cuba,none@nowhere.org,8576806630,harpergarcia@example.com,False

Create code to import the records from the CSV file into the database

    import csv
    from django.shortcuts import render
    from .models import Student

    def import_students_csv(request):
        if request.method == 'POST':
            csv_file = request.FILES['csv_file']

            if not csv_file.name.endswith('.csv'):
                return render(request, 'error.html', {'error_message': 'Invalid file format. Please upload a CSV file.'})

            decoded_file = csv_file.read().decode('utf-8')
            csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')

            # Skip the header row
            next(csv_data)

            fields = ['name', 'user', 'phone', 'email', 'address', 'country', 'payment']
            for row in csv_data:
                data = dict(zip(fields, row))
                student = Student(**data)
                student.save()

            return render(request, 'success.html')

        return render(request, 'import.html')


student.py

    from django.contrib.auth.models import User
    from django.shortcuts import get_object_or_404

    def import_students_csv(request):
        if request.method == 'POST':
            csv_file = request.FILES['csv_file']

            if not csv_file.name.endswith('.csv'):
                return render(request, 'error.html', {'error_message': 'Invalid file format. Please upload a CSV file.'})

            decoded_file = csv_file.read().decode('utf-8')
            csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')

            # Skip the header row
            next(csv_data)

            for row in csv_data:
                create_student(row)
            return render(request, 'success.html')
        return render(request, 'import.html')


    def create_student(row):
        name, user, phone, email, address, country, payment = row
        existing_user = get_object_or_404(User, username=user)
        student, created = Student.objects.get_or_create(
            user=existing_user,
            defaults={
                'name': name,
                'phone': phone,
                'email': email,
                'address': address,
                'country': country,
                'payment': bool(payment)
            }
        )
        if not created:
            student.name = name
            student.phone = phone
            student.email = email
            student.address = address
            student.country = country
            student.payment = bool(payment)
            student.save()

    def create_student2(row):
        name, user, phone, email, address, country, payment = row
        student = Student.objects.create(
            name=name,
            user=user,
            phone=phone,
            email=email,
            address=address,
            country=country,
            payment=bool(payment)
        )   


    def create_student3(row):
        student = Student(**data)
        student.save()
    

    def create_student4(row, fields):
        fields = ['name', 'user', 'phone', 'email', 'address', 'country', 'payment']
        data = dict(zip(fields, row))
        Student.objects.create(**data)


    def create_student5(row, fields):
        fields = ['name', 'user', 'phone', 'email', 'address', 'country', 'payment']
        kwargs = dict(zip(fields, row))
        user = get_object_or_404(User, username=kwargs['user'])
        student, created = Student.objects.get_or_create(user=user)  
        set_student_fields(student, **kwargs)
          

    def set_student_fields(student, **kwargs)   
        for field in kwargs:
            setattr(student, field, kwargs[field])
        student.save()


    def import_students(csv_data):
        fields = ['name', 'user', 'phone', 'email', 'address', 'country', 'payment']
        for row in csv_data:
            data = dict(zip(fields, row))
            create_student(row)


    def import_student_file(csv_data):
        decoded_file = csv_file.read().decode('utf-8')
        csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
        next(csv_data)
        import_students(csv_data)


form.py

    from django.urls import reverse_lazy
    from django.views.generic.edit import FormView
    from .models import Student
    from django import forms

    class ImportStudentsForm(forms.Form):
        csv_file = forms.FileField(label='CSV File', help_text='Please upload a CSV file.')

    class ImportStudentsView(FormView):
        template_name = 'import.html'
        form_class = ImportStudentsForm
        success_url = reverse_lazy('success')

        def form_valid(self, form):
            csv_file = form.cleaned_data['csv_file']

            if not csv_file.name.endswith('.csv'):
                return self.form_invalid(form)

            decoded_file = csv_file.read().decode('utf-8')
            csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')

            next(csv_data)

            for row in csv_data:
                name, user, phone, email, address, country, payment = row
                student = Student.objects.create(
                    name=name,
                    user=user,
                    phone=phone,
                    email=email,
                    address=address,
                    country=country,
                    payment=bool(payment)
                )

            return super().form_valid(form)


templates/import.html

    <form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Import</button>
    </form>

urls.py

    from django.urls import path
    from .views import ImportStudentsView

    urlpatterns = [
        # Other URL patterns
        path('import-students/', ImportStudentsView.as_view(), name='import_students'),
    ]

