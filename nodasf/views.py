from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import get_template
from django.template import Context
from django.template.defaulttags import register
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F, Q
from .models import County, Venue, Agency, Organization, Genre, Issue, City, Party, Level, Event, Politician, Media_Org, Journalist, Local_Link, STF_Hub, STF_Link, STF

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

def media_org(request, slug):
	media = get_object_or_404(Media_Org, pk=slug)
	journalists = Journalist.objects.filter( organization__slug = slug )
	return render(request, 'media-org.html', {'media': media, 'journalists': journalists})
	

def venues(request):
	venues = Venue.objects.all()
	return render(request, 'venues.html', {'venues': venues})
	
def politicians(request):
	politicians = Politician.objects.all()
	return render(request, 'politician.html', {'politicians': politicians})

def issues(request):
	issues = Issue.objects.all()
	return render(request, 'issue.html', {'issues': issues})

def agencies(request):
	agencies = Agency.objects.all()
	return render(request, 'agency.html', {'agencies': agencies})
	
def about(request):
	return render(request, 'about.html')

def organizations(request):
	organizations = Organization.Objects.all()
	return render(request, 'organization.html', {'organizations': organizations})

def journalists(request):
	journalists = Journalist.objects.all()
	return render(request, 'journalist.html', {'journalists': journalists})

	
	