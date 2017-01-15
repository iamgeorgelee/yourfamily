from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .api import FBWebhookViewSet

router = DefaultRouter()

router.register(r'fb', FBWebhookViewSet, base_name='fb')

urlpatterns = [
	url(r'^yourfamily/center/', include(router.urls)),
]
