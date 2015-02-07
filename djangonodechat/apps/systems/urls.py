from django.conf.urls import patterns, include , url
from .views import Login, Home

urlpatterns = patterns ('',
	url(r'^$', Login.as_view() , name='login'),
	url(r'^home/$', Home.as_view() , name='home'),
)