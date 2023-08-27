# Professor Email Edit


class Professor(models.Model):
    user = models.ForeignKey(PrometaUser, on_delete=models.CASCADE,
                             null=True, editable=False, verbose_name=_("User"))
    name = models.CharField(max_length=100, null=True, verbose_name=_("Name"))
    email = models.EmailField(null=True, verbose_name=_('Email Address'))
    
class ProfessorUpdateView(UpdateView):
    model = Professor
    template_name = 'edit.html'
    fields = ('name', 'email')

How do I set the initial value in the form to the user.email?

How do I update the new value of user.email from the form?