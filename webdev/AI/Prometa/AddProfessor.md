# Add Professor to Section

models.py

    class Professor(models.Model):
        user = models.ForeignKey(PrometaUser, on_delete=models.CASCADE, null=True, editable=False, verbose_name=_("User"))
        name = models.CharField(max_length=100, null=True, verbose_name=_("Name"))
        section = models.ManyToManyField(CourseSection, related_name='teacher')


    class CourseSection(models.Model):
        schedule = models.ForeignKey(CoursePeriod, null=True, on_delete=models.CASCADE)
        course = models.ForeignKey(Course, on_delete=models.CASCADE)
        section_number = models.CharField(default='NONE', max_length=20, verbose_name=_("Section Number"))

Create a simple view using TemplateView to display a section.


---

Pass in a list of professors with "professors()"

Add a control to show all professors and a button to add the selected professor to this section.

Write the code to add the professor to the section.

---

section.html

    <form method="post" action="{% url 'add_professor' section.id %}">
        {% csrf_token %}
        <label for="professor">Select Professor:</label>
        <select name="professor" id="professor">
            {% for professor in professors %}
                <option value="{{ professor.id }}">{{ professor.name }}</option>
            {% endfor %}
        </select>
        <button type="submit">Add Professor to Section</button>
    </form>

urls.py

    urlpatterns = [
        path('section/<int:section_id>/', SectionDetailView.as_view(), name='section_detail'),
        path('add_professor/<int:section_id>/', add_professor_to_section, name='add_professor'),
    ]


views.py

    from django.views.generic import TemplateView, UpdateView
    from django.shortcuts import get_object_or_404
    from django.urls import reverse_lazy
    from .models import CourseSection, Professor

    class SectionDetailView(TemplateView):
        template_name = 'section_detail.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            section_id = kwargs.get('section_id')
            section = get_object_or_404(CourseSection, pk=section_id)
            context['section'] = section
            context['professors'] = Professor.objects.all()
            return context


    class AddProfessorToSectionView(RedirectView):
        def get_redirect_url(self, *args, **kwargs):
            section_id = kwargs.get('section_id')
            professor_id = self.request.POST.get('professor')
            section = get_object_or_404(CourseSection, pk=section_id)
            professor = get_object_or_404(Professor, pk=professor_id)
            section.teacher.add(professor)
            return reverse_lazy('section_detail', kwargs={'section_id': section_id})

---

##  OLD CODE


    # views.py
    from django.shortcuts import redirect

    # Function view
    def add_professor_to_section(request, section_id):
        if request.method == 'POST':
            professor_id = request.POST.get('professor')
            section = get_object_or_404(CourseSection, pk=section_id)
            professor = get_object_or_404(Professor, pk=professor_id)
            section.teacher.add(professor)
            return redirect('section_detail', section_id=section_id)

    # UpdateView
    class AddProfessorToSectionView(UpdateView):
        model = CourseSection
        template_name = 'section_detail.html'  # You can use the same template as the detail view
        fields = []  # No fields are being updated, we just need the professor selection

        def form_valid(self, form):
            professor_id = self.request.POST.get('professor')
            professor = get_object_or_404(Professor, pk=professor_id)
            self.object.teacher.add(professor)
            return super().form_valid(form)

        def get_success_url(self):
            return reverse_lazy('section_detail', kwargs={'section_id': self.object.pk})


views.py

    class SectionUpdateView(UpdateView):
        model = CourseSection
        template_name = 'section_edit.html'
        fields = '__all__'
        success_url = reverse_lazy('period_list')

        def get_context_data(self, **kwargs):
            kwargs = super().get_context_data(**kwargs)
            data = dict(professors=Professor.objects.all())
            kwargs.update(data)
            return kwargs


templates/edit.html

    <form action="/section/{{ object.pk }}/assign" method="post">

        {% csrf_token %}

        <label for="professor-select">{% translate "Select Professor to Add:" %}</label>
        <select id="professor-select" name="professor">
            {% for p in profesors %}
            <option value="{{ p.pk }}">{{ p.name }}</option>
            {% endfor %}
        </select>
        <button type="submit" class="btn">
            {% translate "Add Professor to Section" %}
        </button>
    </form>


views.py

    class ProfessorUpdateView(UpdateView):
        model = Professor
        template_name = 'edit.html'
        fields = '__all__'
        success_url = reverse_lazy('professor_list')  

    class SectionUpdateView(UpdateView):
        model = CourseSection
        template_name = 'edit.html'
        fields = '__all__'
        success_url = reverse_lazy('period_list')  

urls.py

    urlpatterns = [
        path('professor/',            ProfessorListView.as_view(),   name='professor_list'),
        path('professor/add',         ProfessorCreateView.as_view(), name='professor_add'),
        path('professor/<int:pk>/',   ProfessorUpdateView.as_view(), name='professor_edit'),
        path('section/',              CourseSectionListView.as_view(),   name='section_list'),
        path('section/add',           CourseSectionCreateView.as_view(), name='section_add'),
        path('section/<int:pk>/',     CourseSectionUpdateView.as_view(), name='section_edit'),
        path('section/<int:section>/<int:professor>', AssignProfessorView.as_view(), name='assign_professor'),
    ]

Is this correct?

---

Add a control to show all professors and a button to add the selected professor to this section.


Add a Redirect View to assign a professor to a section '/section/<int: section><int: professor>'
Show me how to add professors to a CourseSection
