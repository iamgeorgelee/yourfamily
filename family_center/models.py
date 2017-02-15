from __future__ import unicode_literals

from django.db import models


class User(models.Model):
	name = models.CharField(max_length=256, null=True, blank=True)
	facebook_id = models.CharField(max_length=32, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	state = models.PositiveIntegerField(default=0)

class Family(models.Model):
	name = models.CharField(max_length=256)
	admin = models.ForeignKey(User, related_name='family')
	created_at = models.DateTimeField(auto_now_add=True)

class FamilyUserMapping(models.Model):
	family = models.ForeignKey(Family, related_name='fu', null=True)
	user = models.ForeignKey(User, related_name='fu', null=True)
	created_at = models.DateTimeField(auto_now_add=True)

class Bill(models.Model):
	fum = models.ForeignKey(FamilyUserMapping, related_name='pfu', null=True)
	period = models.CharField(max_length=256)
	amount = models.FloatField()

