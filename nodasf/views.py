from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import get_template
from django.template import Context
from django.template.defaulttags import register
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F, Q
from .models import County, Venue, Agency, Organization, Genre, Issue, City, Party, Level, Event, Politician, Media_Org, Journalist, Local_Link, STF_Hub, STF_Link, STF, CongressDistrict, Category

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def index(request):
	local_links = Local_Link.objects.all()[0:15]
	stfs= STF.objects.all().order_by('-date_updated') [0:10]
	events= Event.objects.all().order_by('-date') [0:20]
	return render(request, 'index.html', {'local_links': local_links, 'stfs': stfs, 'events': events})

def media_directory(request):
	medias = Media_Org.objects.all()
	return render(request, 'media-org-directory.html', {'medias': medias})

def media_org(request, id, slug):
	media = get_object_or_404(Media_Org, pk=id)
	journalists = Journalist.objects.filter( organization__id = id )
	return render(request, 'media-org.html', {'media': media, 'journalists': journalists})
	
def venues(request):
	venues = Venue.objects.all()
	return render(request, 'venues.html', {'venues': venues})
	
def venue_part(request, id, slug):
	venue = get_object_or_404(Venue, pk=id)
	events = Event.objects.filter( venue__id = id )
	return render(request, 'venue-part.html', {'venue': venue, 'events': events})
	
def politicians(request):
	politicians = Politician.objects.all()
	return render(request, 'politicians.html', {'politicians': politicians})

def politician_part(request, id, slug):
	politician = get_object_or_404(Politician, pk=id)
	return render(request, 'politician-part.html', {'politician': politician})

def issues(request):
	issues = Issue.objects.all()
	return render(request, 'issue.html', {'issues': issues})

def agencies(request):
	agencies = Agency.objects.all()
	return render(request, 'agency.html', {'agencies': agencies})

def agency_part(request):
	agency = get_object_or_404(Agency, pk=id)
	return render(request, 'agency-part.html', {'agency': agency})
	
def about(request):
	return render(request, 'about.html')

def organizations(request):
	organizations = Organization.Objects.all()
	return render(request, 'organization.html', {'organizations': organizations})

def organization_part(request, id, slug):
	organization = get_object_or_404(Organization, pk=id)
	return render(request, 'organization-part.html', {'organization': organization})
	
def city(request, id, slug):
	city = get_object_or_404(City, pk=id)
	return render(request, 'city.html', {'city': city})	

def county(request, id, slug):
	county = get_object_or_404(County, pk=id)
	return render(request, 'county.html', {'county': county})	

def district(request, id, slug):
	district = get_object_or_404(City, pk=id)
	return render(request, 'district.html', {'district': district})	

def journalists(request):
	journalists = Journalist.objects.all()
	return render(request, 'journalist.html', {'journalists': journalists})

def journalist_part(request, id, slug):
	journalist = get_object_or_404(Journalist, pk=id)
	articles = Local_Link.objects.filter( journalist__id = id)
	return render(request, 'journalist-part.html', {'journalist': journalist, 'articles': articles})

def stf_hub(request, slug, stf_hub_id):
	stf_hub = get_object_or_404(STF_Hub, pk=stf_hub_id)
	stfs = STF.objects.filter( hub__id = stf_hub_id)[0:7]
	stf_links = {
		p: STF_Link.objects.filter(story__id = p.id) for p in stfs
	}	
	return render(request, 'stf-hub.html', {'stf_hub': stf_hub, 'stfs': stf_links})

def stf(request, slug, stf_id):
	stf = get_object_or_404(STF, pk=stf_id)
	stf_links = STF_Link.objects.filter( story__id = stf_id)
	return render(request, 'nodanews/story.html', {'stf': stf, 'stf_links': stf_links})	
	