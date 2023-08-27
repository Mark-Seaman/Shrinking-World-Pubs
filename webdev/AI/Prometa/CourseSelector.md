# Course Selector

class Course(models.Model):
    name = models.CharField(max_length=20, verbose_name=_("Course ID"))
    title = models.CharField(default='NONE', max_length=100, verbose_name=_("Course Title"))
    description = models.TextField(verbose_name=_("Course Description"))
    credit_hours = models.PositiveIntegerField(default='3', verbose_name=_("Credit Hours"))
    is_active = models.BooleanField(default=True, verbose_name=_("Course is Active"))


class StudentRequest(models.Model):
    course_of_interest = models.CharField(max_length=100, null=True, verbose_name=_('Course of Interest'))

write code to create a dropdown selector for courses with course name and title.

---
I already have a View class that adds a request.

class StudentRequestCreateView(CreateView):
    model = StudentRequest
    template_name = 'application.html'
    fields = '__all__'
    success_url = reverse_lazy('request_list')

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['title'] = 'Student Application Form'
        return kwargs

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if not self.request.user.is_authenticated:
            form.fields['payment'].widget = HiddenInput()
            form.fields['application_date'].widget = HiddenInput()
            form.fields['status'].widget = HiddenInput()
            form.fields['status_reason'].widget = HiddenInput()
        return form

Can this logic be added to it?

---

class StudentRequestCreateView(CreateView):
    model = StudentRequest
    template_name = 'application.html'
    fields = '__all__'
    success_url = reverse_lazy('request_list')

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['title'] = 'Student Application Form'
        return kwargs

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['course_of_interest'] = CourseSelectionForm()
        if not self.request.user.is_authenticated:
            form.fields['payment'].widget = HiddenInput()
            form.fields['application_date'].widget = HiddenInput()
            form.fields['status'].widget = HiddenInput()
            form.fields['status_reason'].widget = HiddenInput()
        return form

class CourseSelectionForm(forms.Form):
    course_of_interest = forms.ModelChoiceField(
        queryset=Course.objects.filter(is_active=True),
        empty_label=None,
        to_field_name='name',
        label='Course of Interest',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )


    <div class="form-section">
        <h2>Academics</h2>
        <div class="form-group">
            {{ form.course_of_interest }}
            {{ form.programs_of_interest|as_crispy_field }}
            {{ form.education|as_crispy_field }}
            {{ form.school|as_crispy_field }}
        </div>
    </div>
