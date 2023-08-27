# View Security

A Django app defines a data model for users.

class PrometaUser(AbstractUser):
    is_registrar = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)

Create a simple TemplateView that restricts users to have 'is_registrar'.

