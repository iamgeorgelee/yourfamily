from datetime import datetime

from .models import Member, Family, FamilyUserMapping, FamilyBill, MemberBill
	

class MemberRepo(object):

	def get(self, member_id):
		return Member.objects.get(member_id=member_id)

	def get_by_user_id(self, user_id):
		return Member.objects.get(user_id=user_id)

	def set_fb_messenger_id(self, user_id, fb_messenger_id):
		member = self.get_by_user_id(user_id=user_id)
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

	def create(self, name, plan_type, description=''):
		return Family.objects.create(
			name=name,
			plan_type=plan_type,
			description=description,
		)

	def link_family_member(self, family_id, member_id, admin=False):
		return FamilyUserMapping.objects.create(
			family=family_id,
			member=member_id,
			admin=admin
		)

	def get(self, family_id):
		return Family.objects.get(id=family_id)

	def get_familes_by_member(self, member_id):
		return Family.objects.filter(FamilyUserMapping__member_id=member_id)


class FamilyBillingRepo(object):

	def create(self, family_id, detail):
		return FamilyBill.objects.create(
			family=family_id,
			period_type=detail.get('period_type'),
			total=detail.get('total'),
			year=detail.get('year'),
   			month=detail.get('month'),
		)

	def get(self, family_id):
		return FamilyBill.objects.filter(family_id=family_id)

	def get_last(self, family_id):
		return self.get(family_id).last()

	def get_last_with_member_detail(self, family_id):
		return self.get_last(family_id).select_related()

	def get_latest_bill_by_family_user(self, family_id, user_id):
		return Bill.objects.filter(fum__user_id=user_id, fum__family_id=family_id)

class MemberBillingRepo(object):

	def bulk_create(self, family_bill, members_detail):

		member_bills = [ 
			MemberBill(
				member = detail.get(member_id),
				family_bill = family_bill,
				amount = detail.get('amount'),
				paid = detail.get('paid'),
			) for detail in members_detail]

		MemberBill.objects.bulk_create(member_bills)	

	def update_family_member_bill(self, family_bill_id, member_id, amount, paid):
		bill_obj = MemberBill.objects.get(family_bill_id=family_bill_id, member_id=member_id)

		if amount:
			bill_obj.amount = amount

		if paid != None:
			bill_obj.paid = paid
			bill_obj.paid_date = datetime.now() if paid else None

		bill_obj.save()

	def get_last(self, family_id, member_id):
		return MemberBill.objects.get(family_bill__family_id=family_id, member_id=member_id)


member_repo = MemberRepo()
family_repo = FamilyRepo()
family_billing_repo = FamilyBillingRepo()
member_billing_repo = MemberBillingRepo()

