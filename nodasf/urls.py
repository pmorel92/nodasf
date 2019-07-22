from django.conf.urls import url, include


from . import views
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^media-org-directory/(?P<slug>[\w-]+)/$', views.media_directory, name='media org directory'),	
	]