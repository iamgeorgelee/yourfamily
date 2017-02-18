from django.conf import settings

import facebook

from .repos import MemberRepo, FamilyRepo, FURepo, BillingRepo

member_repo = MemberRepo()
family_repo = FamilyRepo()
fu_repo = FURepo()
billing_repo = BillingRepo()

class MemberService(object):

	def get(self, member_id):
		return member_repo.get(member_id)

	def set_fb_messenger_id(self, user_id, fb_messenger_id):
		return member_repo.set_fb_messenger_id(user_id, fb_messenger_id)

	def set_state_by_fb(self, fb_messenger_id, state):
		return member_repo.set_chat_state(fb_messenger_id, state)

	def get_by_fb_messenger_id(self, fb_messenger_id):
		return member_repo.get_by_fb_messenger_id(fb_messenger_id)


class FamilyService(object):

	def create(self, name, admin_id):
		return family_repo.create(name, admin_id)

class FUService(object):

	def link(self, family_id, user_id):
		return fu_repo.link(family_id, user_id)

class BillingService(object):

	def create_period_bill(self, family_bills):
		return billing_repo.create_period_bill(family_bills)

	def get_latest_bill_family_detail(self, family_id):
		return billing_repo.get_latest_bill_family_detail(family_id)

	def get_latest_bill_by_family_user(self, family_id, user_id):
		return billing_repo.get_latest_bill_by_family_user(family_id, user_id)


# class FacebookService(Object):

# 	app_id = settings.FACEBOOK_APP_ID
# 	secret = settings.FACEBOOK_SECRET

# 	token = facebook.GraphAPI().get_app_access_token(app_id, secret)
# 	graph = facebook.GraphAPI(access_token=token, version='2.8')

# 	def get_user_name_from_id(self, facebook_id)
		
