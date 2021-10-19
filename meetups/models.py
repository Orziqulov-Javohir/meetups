from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.email}'

class Location(models.Model):
    name = models.CharField(max_length=50)
    address  = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.address})'



class Meetup(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    date = models.DateField(blank=True, null=True)
    organizer_email = models.EmailField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images')
    location = models.ForeignKey(Location, on_delete = models.CASCADE, blank=True)
    participant = models.ManyToManyField(participant, blank=True,)
    
    def __str__(self):
        return f'{self.title}'