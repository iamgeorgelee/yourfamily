from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .constants import MONTH_CHOICES
from .constants import PLAN_TYPE_CHOICES
from .constants import PERIOD_TYPE_CHOICES

class Member(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	fb_messenger_id = models.CharField(max_length=256, unique=True, null=True, blank=True)
	chat_state = models.PositiveIntegerField(default=0)

class Family(models.Model):
	name = models.CharField(max_length=256)
	plan_type = models.CharField(max_length=32, choices=PLAN_TYPE_CHOICES)
	created_at = models.DateTimeField(auto_now_add=True)
	description = models.CharField(null=True, blank=True)

class FamilyUserMapping(models.Model):
	family = models.ForeignKey(Family, null=True)
	member = models.ForeignKey(Member, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	admin = models.BooleanField(default=False)

class FamilyBill(models.Model):
	family = models.ForeignKey(Family, null=True)
	period_type = models.CharField(max_length=16, chioces=PERIOD_TYPE_CHOICES, defalut='M')
	total = models.FloatField()
	year = models.IntegerField(blank=True, null=True)
    month = models.CharField(max_length=9, choices=MONTHS_CHOICES, null=True, blank=True)

class MemberBill(models.Model):
	member = models.ForeignKey(Member, null=True)
	family_bill = models.ForeignKey(FamilyBill, null=True)
	amount = models.FloatField()
	paid = models.BooleanField(default=False)
	paid_date = models.DateTimeField(null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.member.save()
