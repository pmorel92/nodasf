from django.contrib import admin

from .models import County, Venue, Agency, Genre, Issue, City, Party, Level, Event, Politician, Media_Org, Journalist, Local_Link, STF, STF_Hub, STF_Link, District, Category, Organization

class Media_OrgAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']

class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'county', 'imageQ']
    
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'venue', 'city', 'date']
    date_hierarchy= 'date'

class VenueAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'county', ]

class AgencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']

class OrgAdmin(admin.ModelAdmin):
    list_display = ['issue', 'category']

admin.site.register(County)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Agency, AgencyAdmin)
admin.site.register(Genre)
admin.site.register(Issue)
admin.site.register(City, CityAdmin)
admin.site.register(Party)
admin.site.register(Level)
admin.site.register(Event, EventAdmin)
admin.site.register(Politician)
admin.site.register(Media_Org, Media_OrgAdmin)
admin.site.register(Journalist)
admin.site.register(Local_Link)
admin.site.register(STF)
admin.site.register(STF_Hub)
admin.site.register(STF_Link)
admin.site.register(District)
admin.site.register(Category)
admin.site.register(Organization, OrgAdmin)