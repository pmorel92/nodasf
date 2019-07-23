from django.conf.urls import url, include


from . import views
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^media-org-directory/$', views.media_directory, name='media org directory'),	
	url(r'^media-org/(?P<slug>[\w-]+)/$', views.media_org, name='media org'),	
	url(r'^journalist/$', views.journalists, name='journalist directors'),
	url(r'^venues/$', views.venues, name="venue directory"),
	url(r'^politicians/$', views.politicians, name="politician directory"),
	url(r'^issues/$', views.issues, name="issue directory"),
	url(r'^agency/$', views.agencies, name="agency directory"),
	url(r'^about/$', views.about, name="about NodaSF"),	
	url(r'^organizations/$', views.organizations, name="organization directory"),	

	]