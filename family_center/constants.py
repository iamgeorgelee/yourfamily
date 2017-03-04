import calendar

MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1,13)]

PLAN_TYPE_CHOICES = (
    ('T-MOBILE', 'T-Mobile'),
)

PERIOD_TYPE_CHOICES = (
	('M', 'monthly'),
	('Y', 'Yearly')
)