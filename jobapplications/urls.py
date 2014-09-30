from django.conf.urls import patterns, url

from jobapplications import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^(?P<job_id>\d+)/block/$', views.block, name='block'),
)


