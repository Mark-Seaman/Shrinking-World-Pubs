Write Python code for a Django data model that holds student data.  

Place all output in a code block.

Allow all fields to be Null

Create the following fields:

### Student

The student is the primary data model in the system.

Fields

* Full Name - text
* Birth date - text
* GovIDNumber - text
* ID Type - text
* Address - text
* Phone - text
* Email - email
* Current Church - text
* Country - text
* ApplicationDate - Date
* Full Name - text
* Birth date - text
* GovIDNumber - text
* ID Type - text
* Course - Course
* Programs - text area

## Django Data Model

Python code for Student

    from django.db import models

    class Student(models.Model):
        full_name = models.CharField(max_length=200)
        birth_date = models.CharField(max_length=10)
        gov_id_number = models.CharField(max_length=20)
        id_type = models.CharField(max_length=20)
        address = models.TextField()
        phone = models.CharField(max_length=20)
        email = models.EmailField()
        current_church = models.CharField(max_length=100)
        country = models.CharField(max_length=50)
        application_date = models.DateField()
        course = models.ForeignKey(Course, on_delete=models.CASCADE)
        programs = models.TextField()

        def __str__(self):
            return self.full_name
