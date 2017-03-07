import calendar

MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1,13)]

PROVIDER_CHOICES = (
    ('T-MOBILE', 'T-Mobile'),
)

PERIOD_TYPE_CHOICES = (
	('M', 'monthly'),
	('Y', 'Yearly')
)


MESSENGEGR_NEW_USER_BUTTONS = {
 	"template_type":"button",
 	"text":"Looks like you are new here! Please sign up with our website. If you already signed up, click log in to start chatting",
	"buttons":[
		{
			"type":"web_url",
			"url":"https://iamgeorgelee.com/yourfamily/signup/",
			"title":"Sign up"
		},
		{
			"type":"account_link",
			"url":"https://iamgeorgelee.com/yourfamily/authorize_from_messenger",
		},
    ]
}