import requests
import json

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.decorators import list_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import permissions

from .services import MemberService

MY_TOKEN = 'my_token'
FB_POST_URL = 'https://graph.facebook.com/v2.6/me/messages'
PAGE_ACCESS_TOKEN = settings.FB_PAGE_ACCESS_TOKEN

member_service = MemberService()

class FBWebhookViewSet(viewsets.ViewSet):
	
	permission_classes = (permissions.AllowAny,)

	@list_route(methods=['get', 'post'], url_path='webhook')
	def webbhook(self, request):
		if request.method == 'GET':
			q_param = request.query_params
			if q_param.get('hub.mode') == 'subscribe' and q_param.get('hub.verify_token') == MY_TOKEN:
				challenge = q_param.get('hub.challenge')
				print challenge 
				return Response(int(challenge), status=status.HTTP_200_OK)
			else:
				return Response('error', status=status.HTTP_403_FORBIDDEN)
		elif request.method == 'POST': # POST
			data = dict(request.data.iteritems())
			print data

			# Make sure this is a page subscription
			if data.get('object') == 'page':

				for entry in data.get('entry'):

					for event in entry.get('messaging'):
						if(event.get('message')):
							self.process_event(event)


			return Response(status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)

	def process_event(self, event):
		message = event.get('message')
		if message.get('text'):

			sender_id = event.get('sender').get('id')
			text = message.get('text')
			member = member_service.get_by_fb_messenger_id(sender_id)
			
			if member:
				reply = 'I do not understand'
				# state = member.chat_state
				self.send_text_message(sender_id, reply)
			else:
				self.send_login_message(sender_id)	

	def contains_ignore_case(self, substring, original_string):
		return substring.upper() in original_string.upper()

	def send_text_message(self, recipient_id, message_text):
		message_data = {}
		recipient = {'id': recipient_id}
		message = {'text': message_text}
		message_data['recipient'] = recipient
		message_data['message'] = message
		self.call_send_api(message_data)

	def send_login_message(self, recipient_id):
		message_data = {}
		recipient = {'id': recipient_id}
		message = {"attachment":{
			"type":"template",
 			"payload":{
 				"template_type":"button",
 				"text":"Looks like you are new here! Please sign up with our website. If you already signed up, click log in to start chatting",
				"buttons":[
						{
							"type":"web_url",
							"url":"https://iamgeorgelee.com/yourfamily/login/",
							"title":"Sign up"
						},
						{
							"type":"account_link",
							"url":"https://iamgeorgelee.com/yourfamily/authorize_from_messenger",
						},
        			]
      			}
    		}}
		message_data['recipient'] = recipient
		message_data['message'] = message
		self.call_send_api(message_data)

	def call_send_api(self, message_data):
		qs = { 'access_token': PAGE_ACCESS_TOKEN }
		res = requests.post(FB_POST_URL,json=message_data, params=qs)
		if res.status_code == 200:
			print 'success'
		else:
			print res.status_code
			print res.text
