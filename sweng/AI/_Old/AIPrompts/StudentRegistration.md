# Student registration view

Sure! Here's a student registration view for the given data models:

    from django.contrib.auth.decorators import login_required
    from django.shortcuts import render, redirect
    from .models import Course, Student
    from .forms import StudentRegistrationForm

    @login_required
    def register_student(request):
        if request.method == 'POST':
            form = StudentRegistrationForm(request.POST)
            if form.is_valid():
                # Create a new Student object
                student = form.save(commit=False)
                student.user = request.user
                student.save()
                return redirect('home')
        else:
            form = StudentRegistrationForm()
        
        return render(request, 'register.html', {'form': form})

In this view, we import the necessary modules and classes from Django, including the `Course` and `Student` models, as well as a hypothetical `StudentRegistrationForm` form. We also use the `login_required` decorator to ensure that only logged-in users can access the registration form.
 
When the view is accessed, it checks if the request method is POST, indicating that the form has been submitted. If that's the case, we initialize the form with the data passed in the request and validate it. If the form is valid, we create a new `Student` object, associate it with the currently logged-in user, and save it to the database. Finally, we redirect the user to the home page.

If the request method is GET, we simply create a new instance of the form and render the `register.html` template, passing the form object as context.

Note that you'll need to have a `register.html` template and a `StudentRegistrationForm` form defined in order for the above code to work properly.