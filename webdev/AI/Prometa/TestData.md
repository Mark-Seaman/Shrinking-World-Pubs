# Test Data Generator

## Common Names

Generate a list of names for people that use common first and last names

    import random

    first_names = ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'Ethan', 'Isabella', 'William', 'Sophia', 'James', 'Charlotte', 'Benjamin', 'Mia', 'Lucas', 'Amelia', 'Mason', 'Harper', 'Evelyn', 'Jacob', 'Abigail']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Perez', 'Taylor', 'Anderson', 'Wilson', 'Jackson', 'Diaz', 'Wright']

    names = []
    for i in range(10):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        names.append(f'{first_name} {last_name}')

    print(names)


## Generator Script

A student record has name, email, phone.

Create test data for 10 students.

Place output as CSV data in a code block.

    import csv
    import random
    import string

    # Generate random names
    first_names = ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'Ethan', 'Isabella', 'William', 'Sophia', 'James', 'Charlotte', 'Benjamin', 'Mia', 'Lucas', 'Amelia', 'Mason', 'Harper', 'Evelyn', 'Jacob', 'Abigail']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Perez', 'Taylor', 'Anderson', 'Wilson', 'Jackson', 'Diaz', 'Wright']
    names = [f'{random.choice(first_names)} {random.choice(last_names)}' for _ in range(10)]

    # Generate random email addresses
    emails = [name.lower().replace(' ', '') + '@example.com' for name in names]

    # Generate random phone numbers
    phones = [''.join(random.choices(string.digits, k=10)) for _ in range(10)]

    # Combine data into list of tuples
    data = list(zip(names, emails, phones))

    # Output data as CSV
    csv_output = [['Name', 'Email', 'Phone']] + data
    for row in csv_output:
        print(','.join(row))


## Test Data

### Contact Info

Name,Email,Phone
Ethan Davis,ethandavis@example.com,9786208345
William Wright,williamwright@example.com,4925170369
Emma Williams,emmawilliams@example.com,1976843509
Sophia Martinez,sophiamartinez@example.com,4972561303
Lucas Garcia,lucasgarcia@example.com,1284956037
Ava Hernandez,avahernandez@example.com,6183920476
Jacob Rodriguez,jacobrodriguez@example.com,2598314076
Mia Anderson,miaanderson@example.com,6417023859
Isabella Smith,isabellasmith@example.com,1340967285
Harper Jones,harperjones@example.com,3942518670


### Academic Programs

Given this Django data model, write code to create 10 records.

class AcademicProgram(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Academic Program"))

Suggest 10 Academic Programs for a Seminary

1. Master of Divinity
2. Master of Arts in Theology
3. Master of Arts in Christian Counseling
4. Master of Arts in Pastoral Ministry
5. Master of Theological Studies
6. Master of Sacred Theology
7. Master of Arts in Spiritual Formation
8. Master of Arts in Intercultural Studies
9. Doctor of Ministry
10. Certificate in Biblical Studies


### Course

Given this Django data model, write code to create 10 records of random test data.

class Course(models.Model):
    name = models.CharField(max_length=20, verbose_name=_("Course Name"))
    title = models.CharField(default='NONE', max_length=100, verbose_name=_("Course Title"))
    description = models.TextField(verbose_name=_("Course Description"))
    credit_hours = models.PositiveIntegerField(default='3', verbose_name=_("Credit Hours"))
    program = models.CharField(default='NONE', max_length=100, verbose_name=_("Academic Program"))

### Course Section

class CourseSection(models.Model):
    semester = models.CharField(max_length=100, verbose_name=_("Academic Semester"))
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    professor = models.CharField(max_length=100, verbose_name=_("Course Professor"))
    section_number = models.CharField(max_length=10, verbose_name=_("Section Number"))
    location = models.CharField(max_length=100, verbose_name=_("Location"))
    moodle_url = models.URLField(verbose_name=_("Moodle URL"))

Given this Django data model, write code to create 10 records of random test data.




