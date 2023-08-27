Consider this Django data model:

class CoursePeriod(models.Model):
    name = models.CharField(max_length=20, default="Fall 2023", verbose_name=_("Course Period Name"))
    start_date = models.DateField(null=True, verbose_name=_("Course Start Date"))
    end_date = models.DateField(null=True, verbose_name=_("Course End Date"))
    enrollment_open = models.DateField(null=True, verbose_name=_("Enrollment Open"))
    enrollment_closed = models.DateField(null=True, verbose_name=_("Enrollment Closed"))
    payment_due = models.DateField(null=True, verbose_name=_("Payment Due"))

Consider this import for CoursePeriod:

def export_course_periods(file_path):
    course_periods = CoursePeriod.objects.all()
    data = {
        'name': [cp.name for cp in course_periods],
        'start_date': [cp.start_date for cp in course_periods],
        'end_date': [cp.end_date for cp in course_periods],
        'enrollment_open': [cp.enrollment_open for cp in course_periods],
        'enrollment_closed': [cp.enrollment_closed for cp in course_periods],
        'payment_due': [cp.payment_due for cp in course_periods],
    }
    df = pd.DataFrame(data)
    date_columns = ['start_date', 'end_date', 'enrollment_open', 'enrollment_closed', 'payment_due']
    df[date_columns] = df[date_columns].astype(str)
    df.to_csv(file_path, index=False)
    print("CoursePeriod records exported successfully.")


Rewrite this function to use the Meta fields to make this a generic export function.

