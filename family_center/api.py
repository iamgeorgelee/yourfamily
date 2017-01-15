from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.decorators import list_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import permissions

MY_TOKEN = 'my_token'

@csrf_exempt
def webhook(request):
	return HttpResponse('hello world')


class FBWebhookViewSet(viewsets.ViewSet):
	
	permission_classes = (permissions.AllowAny,)

	@list_route(methods=['get', 'post'], url_path='webhook')
	def verify_webbhook(self, request):
		if request.method == 'GET':
			q_param = request.query_params
			if q_param.get('hub.mode') == 'subscribe' and q_param.get('hub.verify_token') == MY_TOKEN:
				challenge = q_param.get('hub.challenge')
				print challenge 
				return Response(int(challenge), status=status.HTTP_200_OK)
			else:
				return Response('error', status=status.HTTP_403_FORBIDDEN)
		else: # POST
			data = dict(request.data.iteritems())
                	print data
                	return Response(status=status.HTTP_200_OK)
