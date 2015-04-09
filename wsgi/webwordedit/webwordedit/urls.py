from django.conf.urls import patterns, include, url
from webwordedit.wordlists.api import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
un_bn_in_resource = Un_Verified_bn_in_resource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webwordedit.views.home', name='home'),
    # url(r'^webwordedit/', include('webwordedit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(un_bn_in_resource.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'^wordlists/verify/(?P<lang>[_A-Za-z]+)/(?P<locale>[_A-Za-z]+)/$', 
        'webwordedit.wordlists.views.verify'),
    url(r'^wordlists/verified/(?P<lang>[_A-Za-z]+)/(?P<locale>[_A-Za-z]+)/$', 
        'webwordedit.wordlists.views.verified'),
    url(r'^wordlists/(?P<list_type>[a-z]+)/$', 
        'webwordedit.wordlists.views.wordlists'),
    url(r'^accounts/profile/', 
        'webwordedit.views.loggedin'),
    url(r'^$', 'webwordedit.views.home', name='home'),
)
