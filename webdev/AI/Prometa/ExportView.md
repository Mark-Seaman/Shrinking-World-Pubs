Consider this Django data model:

class Student(models.Model):
    user = models.ForeignKey(PrometaUser, on_delete=models.CASCADE, null=True, editable=False, verbose_name=_("User"))
    name = models.CharField(max_length=100, null=True, verbose_name=_("Name"))
    country = models.CharField(max_length=50, null=True, verbose_name=_("Country"))
    email = models.EmailField(null=True, verbose_name=_("Email"))
    phone = models.CharField(max_length=20, null=True, verbose_name=_("Phone"))
    address = models.TextField(null=True, verbose_name=_("Address"))
    payment = models.BooleanField(default=False, verbose_name=_("Payment"))

Consider this export function:

def export_students(path):
    fields=['name', 'user', 'phone', 'email', 'address', 'country', 'payment']
    return model_export(path, Student, fields=fields)


Build a view to export the student records to a CSV file.

