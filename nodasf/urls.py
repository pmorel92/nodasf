from django.conf.urls import url, include
from django.urls import include, path, re_path

from . import views
urlpatterns = [
	path('', views.index, name='index'),
	path('media-org-directory/', views.media_directory, name='media org directory'),	
	path('media-org-directory/<int:id>/<slug:slug>/', views.media_org, name='media org'),	
	path('journalist/', views.journalists, name='journalist directory'),
	path('journalist/<int:id>/<slug:slug>/', views.journalist_part, name='specific journalists'),
	path('venues/', views.venues, name="venue directory"),
	path('venues/<int:id>/<slug:slug>/', views.venue_part, name='Specific venue'),
	path('politicians/', views.politicians, name="politician directory"),
	path('politicians/<int:id>/<slug:slug>/', views.politician_part, name="politician particular"),	
	path('issues/', views.issues, name="issue directory"),
	path('issues/<int:id>/<slug:slug>/', views.issue_part, name="specific issue"),
	path('agencies/', views.agencies, name="agency directory"),
	path('agency/<int:id>/<slug:slug>/', views.agency_part, name="agency particular"),	
	path('about/', views.about, name="about NodaSF"),	
	path('organizations/', views.organizations, name="organization directory"),	
	path('organizations/<int:id>/<slug:slug>/', views.organization_part, name="organization particular"),	
	path('story/<int:id>/<slug:slug>/', views.stf, name="story to follow"),
	path('hub/<int:id>/<slug:slug>/', views.stf_hub, name="story hub"),
	path('city/<int:id>/<slug:slug>/', views.city, name="city"),
	path('county/<int:id>/<slug:slug>/', views.county, name="county"),
	path('district/<int:id>/<slug:slug>/', views.district, name="district"),
	path('event/<int:id>/<slug:slug>/', views.event, name="event"),
	path('events/', views.events_hub, name="events hub"),
	path('events/genre/<int:id>/<slug:slug>/', views.events_genre, name="events by genre"),
	]