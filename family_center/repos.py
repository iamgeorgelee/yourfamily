from .models import Member, Family, FamilyUserMapping, Bill
	

class MemberRepo(object):

	def get(self, member_id):
		return Member.objects.get(member_id=member_id)

	def set_fb_messenger_id(self, member_id, fb_messenger_id):
		member = self.get(member_id=member_id)
		if not member:
			return None
		member.fb_messenger_id = fb_messenger_id
		member.save()
		return member
		
	def get_by_fb_messenger_id(self, fb_messenger_id):
		try:
			return Member.objects.get(fb_messenger_id=fb_messenger_id)
		except Member.DoesNotExist:
			return None

	def set_chat_state(self, fb_messenger_id, state):
		member = self.get_by_fb_messenger_id(fb_messenger_id=fb_messenger_id)
		if not member:
			return None
		member.state = state
		member.save()
		return member

class FamilyRepo(object):

	def create(self, name, admin_id):
		return Family.objects.create(
			name=name,
			admin=admin_id,
		)

class FURepo(object):

	def link(self, family_id, member_id):
		return FamilyUserMapping.objects.create(
			family=family_id,
			member=member_id,
		)

class BillingRepo(object):

	def create_period_bill(self, family_bills):
		
		bills = list()
		for bill in family_bills:
			bill = Bill(
				fum=bill.get('fum_id'),
				period=bill.get('period'),
				amount=bill.get('amount')
			)
			bills.append(bill)
		Bill.objects.bulk_create(bills)

	def get_latest_bill_family_detail(self, family_id):
		return Bill.objects.filter(fum__family_id=family_id)

	def get_latest_bill_by_family_user(self, family_id, user_id):
		return Bill.objects.filter(fum__user_id=user_id, fum__family_id=family_id)
