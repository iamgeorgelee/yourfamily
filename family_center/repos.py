from .models import User, Family, FamilyUserMapping, Bill
	

class UserRepo(Object):
	def create(self, name, fb_id):
		return User.objects.create(
			name=name,
			facebook_id=fb_id,
			state=0
		)

	def get_or_create(self, fb_id):

		if User.objects.filter(facebook_id=fb_id).exist():
			return User.objects.get(facebook_id=fb_id)
		else 
			return self.create('', fb_id)

	def set_state(self, fb_id, state):
		user = User.objects.get(facebook_id=fb_id)
		user.state = state
		user.save()
		return user

	def update_by_fb(self, fb_id, name, state):
		user = User.objects.get(facebook_id=fb_id)
		user.name = name
		user.state = state
		user.save()
		return user


class FamilyRepo(Object):

	def create(self, name, admin_id):
		return Family.objects.create(
			name=name,
			admin=admin_id,
		)

class FURepo(Object):

	def link(self, family_id, user_id):
		return FamilyUserMapping.objects.create(
			family=family_id,
			user=user_id,
		)

class BillingRepo(Object):

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
