from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Member(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	fb_messenger_id = models.CharField(max_length=256, unique=True, null=True, blank=True)
	chat_state = models.PositiveIntegerField(default=0)

class Family(models.Model):
	name = models.CharField(max_length=256)
	admin = models.ForeignKey(Member, related_name='family')
	created_at = models.DateTimeField(auto_now_add=True)

class FamilyUserMapping(models.Model):
	family = models.ForeignKey(Family, related_name='fu', null=True)
	member = models.ForeignKey(Member, related_name='fu', null=True)
	created_at = models.DateTimeField(auto_now_add=True)

class Bill(models.Model):
	fum = models.ForeignKey(FamilyUserMapping, related_name='pfu', null=True)
	period = models.CharField(max_length=256)
	amount = models.FloatField()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.member.save()
