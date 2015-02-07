from django.conf.urls import patterns, include , url
from .views import Add_Comment

urlpatterns = patterns ('',
	url(r'^add-comment/$', Add_Comment , name='add-comment'),
)