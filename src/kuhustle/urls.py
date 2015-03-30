from django.conf.urls import patterns, include, url
from django.contrib import admin
urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', 'challange.views.users', name='users'),
    url(r'^jobs/', 'challange.views.jobs', name='jobs'),
    url(r'^bids/', 'challange.views.bids', name='bids'),
    url(r'^(?P<n>\w+)/$', 'challange.views.name', name='name'),
    )
