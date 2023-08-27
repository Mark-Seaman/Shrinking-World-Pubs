# StudentRequest Form

ID_CHOICES = [
        ('residency', _('Residency Card')),
        ('national', _('National ID Card')),
        ('passport', _('Passport')),
        ('socsec', _('Social Security')),
        ('other', _('Other')),
    ]

class StudentRequest(models.Model):
    first_name = models.CharField(max_length=100, null=True, verbose_name=_('First Name'))
    first_last_name = models.CharField(max_length=100, null=True, verbose_name=_('First Last Name'))
    second_last_name = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Second Last Name'))
    course_of_interest = models.CharField(max_length=100, null=True, verbose_name=_('Course of Interest'))
    country = models.CharField(max_length=50, null=True, verbose_name=_('Country of Residence'))    
    gov_id_number = models.CharField(max_length=20, null=True, verbose_name=_('Government ID Number'))
    id_type = models.CharField(max_length=20, choices=ID_CHOICES, null=True, verbose_name=_('ID Type'))
    birth_date = models.CharField(max_length=10, null=True, verbose_name=_('Birth Date'))


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = StudentRequest
        fields = '__all__'

    course_of_interest = forms.ModelChoiceField(
        queryset=Course.objects.filter(is_active=True).order_by('name'),
        empty_label='',
        to_field_name='name',
        label='Course of Interest',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )


class StudentRequestCreateView(CreateView):
    model = StudentRequest
    template_name = 'application.html'
    form_class = ApplicationForm
    success_url = reverse_lazy('request_list')



write code for a calendar widget for birthdate

write code to create a dropdown selector for ID_CHOICES.
write code for a country widget for country


