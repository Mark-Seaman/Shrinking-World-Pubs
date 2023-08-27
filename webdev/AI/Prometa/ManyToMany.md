# Django ManyToMany

Consider these data models


class CourseSection(models.Model):
    title = models.CharField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Professor(models.Model):
    user = models.ForeignKey(PrometaUser, on_delete=models.CASCADE, null=True, editable=False, verbose_name=_("User"))
    name = models.CharField(max_length=100)
    section = models.ManyToManyField(CourseSection, related_name='teacher')

Show me how to add multiple professors to a class and multiple classes to a professor.

---

To add multiple professors to a class and multiple classes to a professor using the given data models, you can use the Django ORM (Object-Relational Mapping) and its methods to create and associate the objects. Here's how you can do it:

1. Create Course and CourseSection objects:

course = Course.objects.get(id=<course_id>)
course_section_1 = CourseSection.objects.create(title="Section 1", course=course)
course_section_2 = CourseSection.objects.create(title="Section 2", course=course)


2. Create Professor objects:

professor_1 = Professor.objects.create(user=<user_object_1>, name="Professor 1")
professor_2 = Professor.objects.create(user=<user_object_2>, name="Professor 2")


3. Add multiple professors to a class:

# Add professors to the course section
course_section = CourseSection.objects.get(id=<course_section_id>)
course_section.teacher.add(professor_1, professor_2)


4. Add multiple classes to a professor:

# Add course sections to the professor
professor = Professor.objects.get(id=<professor_id>)
professor.section.add(course_section_1, course_section_2)


# class professors
section = CourseSection.objects.get(id=<course_section_id>)
for professor in section.teacher.all():
    print(professor.name)

# Sections taught
professor = Professor.objects.get(id=<professor_id>)
for section in professor.section.all():
    print(section.title)
