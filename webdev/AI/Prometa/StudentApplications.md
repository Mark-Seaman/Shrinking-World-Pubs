You are creating a student registration system for an online seminary.

Use the following Django Data Model to create matching test data.

Create a Python program to generate the test data.

class StudentRequest(models.Model):

    STATUS_CHOICES = [
        ('accepted', _('Accepted')),
        ('pending', _('Pending')),
        ('rejected', _('Rejected')),
    ]

    application_date = models.DateField(null=True, verbose_name=_("Today's Date"))
    course_of_interest = models.CharField(max_length=100, null=True, verbose_name=_('Course of Interest'))
    programs_of_interest = models.TextField(null=True, verbose_name=_('Programs of Interest'))

    # Identification
    first_name = models.CharField(max_length=100, null=True, verbose_name=_('First Name'))
    first_last_name = models.CharField(max_length=100, null=True, verbose_name=_('First Last Name'))
    second_last_name = models.CharField(max_length=100, null=True, verbose_name=_('Second Last Name'))
    birth_date = models.CharField(max_length=10, null=True, verbose_name=_('Birth Date'))
    country = models.CharField(max_length=50, null=True, verbose_name=_('Country of Residence'))
    gov_id_number = models.CharField(max_length=20, null=True, verbose_name=_('Government ID Number'))
    id_type = models.CharField(max_length=20, null=True, verbose_name=_('ID Type'))
    email = models.EmailField(null=True, verbose_name=_('Email Address'))
    phone = models.CharField(max_length=20, null=True, verbose_name=_('Phone'))
    phone_type = models.IntegerField(null=True, verbose_name=_('Phone Type'))
    whatsapp = models.BooleanField(default=False, verbose_name=_('WhatsApp enabled?'))
    
    # Academic History
    education = models.IntegerField(null=True, verbose_name=_('Educational History'))
    school = models.CharField(max_length=200, null=True, verbose_name=_('Degree School'))
    referral = models.TextField(null=True, verbose_name=_('Referral Source'))
    church = models.CharField(max_length=100, null=True, verbose_name=_('Current Church'))
    faith = models.TextField(null=True, verbose_name=_('Faith Journey'))
    faith_years = models.IntegerField(null=True, verbose_name=_('Length of Belief'))
    gifts = models.TextField(null=True, verbose_name=_('Spiritual Gifts'))
    ministry = models.TextField(null=True, verbose_name=_('Ministry Work Experience'))
    passion = models.TextField(null=True, verbose_name=_('Ministry Passion'))

    # Payment Made
    payment = models.BooleanField(default=False, verbose_name=_("Payment"))
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name=_('Status')
    )
    status_reason = models.CharField(default='OK', max_length=200)
 