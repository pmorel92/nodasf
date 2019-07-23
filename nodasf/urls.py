from django.conf.urls import url, include
from django.urls import include, path, re_path

from . import views
urlpatterns = [
	path('', views.index, name='index'),
	path('media-org-directory/', views.media_directory, name='media org directory'),	
	path('media-org-directory/<int:id>/(<slug:slug>/', views.media_org, name='media org'),	
	url(r'^journalist/$', views.journalists, name='journalist directors'),
	url(r'^venues/$', views.venues, name="venue directory"),
	url(r'^politicians/$', views.politicians, name="politician directory"),
	url(r'^issues/$', views.issues, name="issue directory"),
	url(r'^agency/$', views.agencies, name="agency directory"),
	url(r'^about/$', views.about, name="about NodaSF"),	
	url(r'^organizations/$', views.organizations, name="organization directory"),	

	]