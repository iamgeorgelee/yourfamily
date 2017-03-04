from django.conf import settings

import facebook

from .repos import member_repo, family_repo, member_billing_repo, family_billing_repo

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

	def create(self, name, admin_id, plan_type):
		return family_repo.create(name, admin_id, plan_type)

	def add_member(self, family_id, memeber_id):
		return family_repo.link_family_member(family_id, memeber_id)

	def get(self, family_id):
		return family_repo.get(family_id)

	def get_with_members(self, family_id):
		return family_repo.get(family_id)

	def get_familes_by_member(self, member_id):
		return family_repo.get_familes_by_member(member_id)


class BillingService(object):

	def create(self, family_id, family_bill, members_detail):
		family_bill_obj = billing_repo.create(family_id, family_bill)
		if members_detail:
			member_billing_repo.bulk_create(family_bill_obj.id, members_detail)
		return family_bill_obj

	def update_family_member_bill_amount(self, family_bill_id, member_id, amount):
		return member_billing_repo.update_family_member_bill(family_bill_id, member_id, amount=amount)

	def bill_paid(self, family_bill_id, member_id, paid=True):
		return member_billing_repo.update_family_member_bill(family_bill_id, member_id, paid=paid)

	def get_latest_bill_by_family(self, family_id):
		return family_billing_repo.get_last(family_id)

	def get_latest_bill_detail_by_family(self, family_id):
		return family_billing_repo.get_last_with_member_detail(family_id)

	def get_latest_bill_by_family_member(self, family_id, member_id):
		return member_billing_repo.get_last(family_id, member_id)

	def get_bills_by_family(self, family_id):
		return family_billing_repo.get(family_id)

# class FacebookService(Object):

# 	app_id = settings.FACEBOOK_APP_ID
# 	secret = settings.FACEBOOK_SECRET

# 	token = facebook.GraphAPI().get_app_access_token(app_id, secret)
# 	graph = facebook.GraphAPI(access_token=token, version='2.8')

# 	def get_user_name_from_id(self, facebook_id)
		
