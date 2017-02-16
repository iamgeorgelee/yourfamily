from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .api import FBWebhookViewSet

from django.contrib.auth import views as auth_views

import views as home_views

router = DefaultRouter()

router.register(r'fb', FBWebhookViewSet, base_name='fb')

urlpatterns = [
	url(r'^center/', include(router.urls)),

	url(r'^$', home_views.home, name='home'),
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, name='logout'),
	url(r'^signup/$', home_views.signup, name='signup'),
	url(r'^settings/$', home_views.settings, name='settings'),
	url(r'^settings/password/$', home_views.password, name='password'),
	url(r'^oauth/', include('social_django.urls', namespace='social')),
]
