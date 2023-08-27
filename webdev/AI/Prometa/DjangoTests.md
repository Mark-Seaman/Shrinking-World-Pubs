Here is the Python code for a Django data model:

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse_lazy

class PrometaUser(AbstractUser):
    name = models.CharField(max_length=200, default="None", null=True)
    is_registrar = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}' 

    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse_lazy('user_list')

    @property
    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]


Please implement a  Django test suite for the PrometaUser data model.

---

Here is the Python code for a Django data model:

    class Student(models.Model):
        user = models.ForeignKey(PrometaUser, on_delete=models.CASCADE)
        full_name = models.CharField(max_length=200)
        birth_date = models.CharField(max_length=10)
        gov_id_number = models.CharField(max_length=20)
        id_type = models.CharField(max_length=20)
        address = models.TextField()
        phone = models.CharField(max_length=20)
        church = models.CharField(max_length=100)
        country = models.CharField(max_length=50)
        application_date = models.DateField()

Please implement a  Django test suite for the Student data model.