from django.contrib import admin
from django.db import models
from .models import Meetup, Location,participant
# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title','date', 'location')
    list_filter = ('date','location') 
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(participant)