I am trying to create a login with email.

settings.py

    LOGOUT_REDIRECT_URL = '/login/'

urls.py

    urlpatterns = [
        path('',                 PrometaUserView.as_view(),    name='home'),
        path('login/',           login_email_view,             name='login'),
    ]

views.py

    def login_email_view(request):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = get_user_model().objects.filter(email=email).first()
            if user and user.check_password(password):
                login(request, user)
                return redirect(reverse_lazy('home'))
            else:
                error_message = "Invalid credentials. Please try again."
                return render(request, 'login.html', {'error_message': error_message})
        return render(request, 'login.html')

tests.py

    class LoginTest(DjangoTest):
        def setUp(self):
            self.client = Client()
            self.username = 'testuser'
            self.email = 'testuser@example.com'
            self.password = 'testpassword'
            self.user = get_user_model().objects.create_user(
                email=self.email,
                username=self.username,
                password=self.password
            )
            self.login_username_url = '/login_username/'
            self.login_email_url = '/login/'
            
        def test_login_email(self):
            response = self.client.post(
                self.login_email_url, {'email': self.email, 'password': self.password})
            # Expecting a redirect after successful login
            self.assertEqual(response.status_code, 302)
            # Replace with your expected redirect URL
            self.assertRedirects(response, reverse_lazy(''))

Show me how to setup the redirect logic so that the test passes.

