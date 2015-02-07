from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangonodechat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^', include('djangonodechat.apps.systems.urls', namespace='systems')),
    url(r'^', include('djangonodechat.apps.users.urls', namespace='users')),
    url(r'^', include('djangonodechat.apps.comments.urls', namespace='comments')),
)
