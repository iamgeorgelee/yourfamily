from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

@csrf_exempt
def webhook(request):
	return HttpResponse('hello world')

