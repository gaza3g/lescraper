from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^jobapplications/', include('jobapplications.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
