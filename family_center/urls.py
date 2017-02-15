from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .api import FBWebhookViewSet

from django.contrib.auth import views as auth_views

import .views as home_views

router = DefaultRouter()

router.register(r'fb', FBWebhookViewSet, base_name='fb')

urlpatterns = [
	url(r'^center/', include(router.urls)),

	url(r'^$', home_views.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
git 