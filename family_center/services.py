from django.conf import settings

import facebook

from .repos import UserRepo, FamilyRepo, FURepo, BillingRepo

user_repo = UserRepo()
family_repo = FamilyRepo()
fu_repo = FURepo()
billing_repo = BillingRepo()

class UserService(object):

	def create(self, name, fb_id):
		return user_repo.create(name, fb_id)

	def get_or_create(self, fb_id):
		return user_repo.get_or_create(fb_id)

	def get_state_by_fb(self, fb_id):
		return self.get_or_create(fb_id).state

	def set_state_by_fb(self, fb_id, state):
		return user_repo.set_state(fb_id, state)

	def update_by_fb(self, fb_id, name, state):
		return user_repo.update_by_fb(fb_id, name, state)

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
		
