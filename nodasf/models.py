from django.db import models
from datetime import datetime
from django.db.models.aggregates import Count


class County(models.Model):
    name = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='media/stock', default='', blank=True)    
    slug = models.SlugField(max_length=100, default=' ')
    
    def __str__(self):
        return self.name    
    class Meta:
        ordering = ('name',)

class Category(models.Model):
    name = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.name    
        
class Agency(models.Model):
    name = models.CharField(max_length=100, default='')
    picture = models.ImageField(upload_to='media/stock', default=" ")
    homepage = models.CharField(max_length=300, default='')
    description = models.TextField()
    category = models.ForeignKey(
        'Category',
        null=True,
        on_delete=models.PROTECT)
    slug = models.SlugField(max_length=100, default=' ')
    
    def __str__(self):
        return self.name    
    class Meta:
        ordering = ('name',)

class Organization(models.Model):
    name = models.CharField(max_length=100, default='')
    picture = models.ImageField(upload_to='media/stock', default=" ")
    homepage = models.CharField(max_length=300, default='')
    description = models.TextField()
    category = models.ForeignKey(
        'Category',
        null=True,    
        on_delete=models.PROTECT)    
    slug = models.SlugField(max_length=100, default=' ')
    
    def __str__(self):
        return self.name    
    class Meta:
        ordering = ('name',)

class Genre(models.Model):
    name = models.CharField(max_length=100, default='')
    slug = models.SlugField(max_length=100, default=' ')

    def __str__(self):
        return self.name    

class Issue(models.Model):
    name = models.CharField(max_length=100, default='')
    imageQ = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/stock', default='', blank=True)
    slug = models.SlugField(max_length=100, default=' ')

    def __str__(self):
        return self.name    
    class Meta:
        ordering = ('name',)

class City(models.Model):
    name = models.CharField(max_length=100, default='')
    homepage = models.CharField(max_length=300, default=' ')    
    county = models.ForeignKey(
        'County',
        on_delete=models.PROTECT,)    
    imageQ = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/stock', default='', blank=True)
    slug = models.SlugField(max_length=100, default=' ')

    def __str__(self):
        return self.name 
    class Meta:
        ordering = ('name',)        
        
class Party(models.Model):
    name = models.CharField(max_length=100, default='')
    slug = models.SlugField(max_length=100, default=' ')

    def __str__(self):
        return self.name    

class Level(models.Model):
    name = models.CharField(max_length=100, default='')
    slug = models.SlugField(max_length=100, default=' ')

    def __str__(self):
        return self.name    
        
class District(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.TextField(default=' ')    
    county = models.ManyToManyField('County')
    cities = models.ManyToManyField('City')
    image = models.ImageField(upload_to='media/stock', default='', blank=True)    
    level = models.ForeignKey(
        'Level',
        default=1,
        on_delete=models.PROTECT,)
    slug = models.SlugField(max_length=100, default=' ')    
  
    def __str__(self):
        return self.name   
    class Meta:
        ordering = ('name',)  
        
class Venue(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.TextField(default=' ')
    homepage = models.CharField(max_length=300, default=' ')    
    city = models.ForeignKey(
        'City',
        on_delete=models.PROTECT,)     
    county = models.ForeignKey(
        'County',
        blank=True,
        null=True,
        on_delete=models.PROTECT,)
    imageQ = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/stock', default='', blank=True)
    slug = models.SlugField(max_length=100, default=' ')

    def __str__(self):
        return self.name    
    class Meta:
        ordering = ('name',)
        
class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    city = models.ForeignKey(
        'City',
        on_delete=models.PROTECT,) 
    county = models.ForeignKey(
        'County',
        blank=True,
        null=True,        
        on_delete=models.PROTECT,)
    free = models.BooleanField(default=False)
    cost = models.CharField(max_length=100, default='', blank=True)
    homepage = models.CharField(max_length=200, default='', blank=True)
    genre = models.ForeignKey(
        'Genre',
        on_delete=models.PROTECT,)
    description = models.TextField()
    venue = models.ForeignKey(
        'Venue',
        default=1,
        on_delete=models.PROTECT,)    
    imageQ = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/stock', default='', blank=True)
    slug = models.SlugField(max_length=100, default=' ')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date',)  

class Politician(models.Model):
    name = models.CharField(max_length=100, default='')
    party = models.ForeignKey(
        'Party',
        on_delete=models.PROTECT,)
    level = models.ForeignKey(
        'Level',
        on_delete=models.PROTECT,)
    county = models.ForeignKey(
        'County',
        blank=True,    
        on_delete=models.PROTECT,)
    district = models.ForeignKey(
        'District',
        null=True,
        on_delete=models.PROTECT)        
    picture = models.ImageField(upload_to='media/faces', default=" ")
    homepage = models.CharField(max_length=300, default='')
    description = models.TextField()
    upcoming = models.ForeignKey(
        'Event',
        on_delete=models.PROTECT,)    
    slug = models.SlugField(max_length=100, default=' ')

    def __str__(self):
        return self.name    

class Media_Org(models.Model):
    name = models.CharField(max_length=100, default='')
    home_page = models.CharField(max_length=200, default='')
    date_founded = models.DateField(default='1956-02-27')
    logo = models.ImageField(upload_to='media/logos')
    description = models.TextField()
    city = models.ForeignKey(
        'City',
        on_delete=models.PROTECT,) 
    county = models.ForeignKey(
        'County',
        blank=True,    
        on_delete=models.PROTECT,)
    slug = models.SlugField(max_length=100, default=' ')

    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)
        
class Journalist(models.Model):
    name = models.CharField(max_length=200, default='')
    contact = models.CharField(max_length=200, default='')
    organization = models.ForeignKey(
        'Media_Org',
        on_delete=models.PROTECT,)
    bio = models.TextField(default='bio goes here')
    picture = models.ImageField(upload_to='media/faces', default=" ")
    slug = models.SlugField(max_length=100, default=' ')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)


class Local_Link(models.Model):
    url = models.CharField(max_length=300, default='')
    headline = models.CharField(max_length=150, default='')
    media = models.ForeignKey(
        'Media_Org',
        on_delete=models.CASCADE,)
    posted = models.DateTimeField(default=datetime.now, blank=True)
    county = models.ForeignKey(
        'County',
        blank=True,    
        on_delete=models.PROTECT,)
    city = models.ForeignKey(
        'City',
        on_delete=models.PROTECT,
        blank=True)
    issue = models.ForeignKey(
        'Issue',
        on_delete=models.PROTECT,
       null=True,    
        blank=True,)        
    journalist = models.ForeignKey('Journalist',
    null=True,
    blank=True,
    on_delete=models.PROTECT,)
    imageQ = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/stock', default='', blank=True)

    def __str__(self):
        return "{}/{}".format(self.headline, self.media)

    class Meta:
        ordering = ('-posted',)

class STF_Hub(models.Model):
    name = models.CharField(max_length=100, default='')
    banner = models.ImageField(upload_to='media/stock')
    credit = models.CharField(max_length=200, default='')
    county = models.ForeignKey(
        'County',
        blank=True,    
        on_delete=models.PROTECT,)
    city = models.ForeignKey(
        'City',
        blank=True,
        on_delete=models.PROTECT,)    
    date_updated = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(default='', blank=True)
    issue = models.ForeignKey(
        'Issue',
        null=True,        
        on_delete=models.PROTECT,
        blank=True,)        
    slug = models.SlugField(max_length=200, default=' ') 

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('-date_updated',)        
        
class STF(models.Model):
    headline = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/stock', default='')
    credit = models.CharField(max_length=200, default='')     
    update = models.TextField()
    date_updated = models.DateTimeField()
    videoQ = models.BooleanField(default=False)
    video = models.CharField(max_length=500, default='', blank=True) 
    hub= models.ForeignKey(
        'STF_Hub',
        on_delete=models.PROTECT)
    county = models.ForeignKey(
        'County',
        blank=True,    
        on_delete=models.PROTECT,)
    city = models.ForeignKey(
        'City',
        blank=True,
        on_delete=models.PROTECT,)
    issue = models.ForeignKey(
        'Issue',
       null=True,    
        on_delete=models.PROTECT,
        blank=True,)            
    slug = models.SlugField(max_length=200, default=' ') 

    def __str__(self):
        return "{}/{}".format(self.headline, self.hub)  

class STF_Link(models.Model):
    url = models.CharField(max_length=300, default='', blank=True)
    title = models.CharField(max_length=150, default='', blank=True)
    media = models.ForeignKey(
        'Media_Org',
        on_delete=models.CASCADE,)
    story = models.ForeignKey(
        'STF',
        on_delete=models.CASCADE,)
    def __str__(self):
        return "{}/{}".format(self.id, self.story)
