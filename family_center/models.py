from __future__ import unicode_literals

from django.db import models


class User(models.Model):
	name = models.CharField(max_length=256)
	facebook_id = models.CharField(max_length=32)
	created_at = models.DateTimeField(auto_now_add=True)

class Family(models.Model):
	name = models.CharField(max_length=256)
	admin = models.CharField(mac_length=32)
	created_at = models.DateTimeField(auto_now_add=True)

class FamilyUserMapping(models.Model):
	family_id = models.PositiveIntegerField()
	user_id = models.PositiveIntegerField()
	created_at = models.DateTimeField(auto_now_add=True)

class Period(models.Model):
	name = models.CharField(mac_length=32)
	total = models.IntegerField()

class PeriodFUMapping(models.Model):
	fum = models.ForeignKey(FamilyUserMapping, related_name='pfu')
	period = models.ForeignKey(Period, related_name='pfu')
	name = models.CharField(max_length=32)
	amount = models.IntegerField()

