Given these data models

    class Student(models.Model):
        user = models.ForeignKey(PrometaUser, on_delete=models.CASCADE, null=True, editable=False, verbose_name=_("User"))
        name = models.CharField(max_length=100, null=True, verbose_name=_("Name"))
        country = models.CharField(max_length=50, null=True, verbose_name=_("Country"))
        phone = models.CharField(max_length=20, null=True, verbose_name=_("Phone"))
        address = models.TextField(null=True, verbose_name=_("Address"))
        payment = models.BooleanField(null=True, verbose_name=_("Payment"))

    class PrometaUser(AbstractUser):
        name = models.CharField(max_length=200, default="None", null=True)
        is_registrar = models.BooleanField(default=False)
        is_student = models.BooleanField(default=False)
        is_professor = models.BooleanField(default=False)

Create code to export the records from the database to a CSV file (data/students.csv) 

Pass in fields=['user','name','email'] as an argument.

