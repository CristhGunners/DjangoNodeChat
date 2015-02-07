from django.conf.urls import patterns, include , url
from .views import Logout

urlpatterns = patterns ('',
	url(r'^logout/$', Logout , name='logout'),
)