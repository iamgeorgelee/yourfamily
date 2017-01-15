from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.decorators import list_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

MY_TOKEN = 'my_token'

@csrf_exempt
def webhook(request):
	return HttpResponse('hello world')


class FBWebhookViewSet(viewsets.ViewSet):

	@detail_route(methods=['get'], url_path='webhook')
	def verify_webbhook(self, request):
		q_param = request.query_params
		if q_param.get('hub.mode') == 'subscribe' and q_param.get('hub.verify_token') == MY_TOKEN:
			return Response(q_param.get('hub.challenge'), status=status.HTTP_200_OK)
		else
			return Response('error', status=status.HTTP_403_OK)
		

	@detail_route(methods=['post'], url_path='webhook')
	def webhook(self, request):
		data = dict(request.data.iteritems())
		if not data.get('end_date'):
			data['end_date'] = None

		return Response(serializer.data, status=status.HTTP_201_CREATED)