
from .api import webhook

urlpatterns = patterns(
	'',
	url(r'^webhook/', webhook),
)
