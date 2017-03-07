import requests

from django.conf import settings

from .constants import MESSENGEGR_NEW_USER_BUTTONS

FB_POST_URL = 'https://graph.facebook.com/v2.6/me/messages'
PAGE_ACCESS_TOKEN = settings.FB_PAGE_ACCESS_TOKEN

class FacebookMessenger(object):

	def call_send_api(self, message_data):
		qs = { 'access_token': PAGE_ACCESS_TOKEN }
		res = requests.post(FB_POST_URL,json=message_data, params=qs)
		if res.status_code == 200:
			print 'success'
		else:
			print res.status_code
			print res.text
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
 			"payload": MESSENGEGR_NEW_USER_BUTTONS
    		}
    	}
		message_data['recipient'] = recipient
		message_data['message'] = message
		self.call_send_api(message_data)

	def get_psid(self, account_linking_token):
		qs = { 'access_token': PAGE_ACCESS_TOKEN, 'fields': 'recipient', 'account_linking_token': account_linking_token }
		res = requests.get('https://graph.facebook.com/v2.6/me', params=qs)
		if res.status_code == 200:
			payload = json.loads(res.text)
			return payload.get('recipient')
		else:
			print res.status_code
			print res.text
			return None

facebook_messenger = FacebookMessenger()